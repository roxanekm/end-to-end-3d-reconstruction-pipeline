import open3d as o3d
import numpy as np


def load_pointcloud(path):
    pcd = o3d.io.read_point_cloud(path)

    if pcd is None or len(pcd.points) == 0:
        raise ValueError("Empty point cloud")

    return pcd


def clean_pointcloud(pcd):
    pcd, _ = pcd.remove_statistical_outlier(
        nb_neighbors=20,
        std_ratio=2.0
    )

    pcd = pcd.voxel_down_sample(voxel_size=0.01)

    return pcd


def estimate_normals(pcd):
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(
            radius=0.1,
            max_nn=30
        )
    )

    pcd.normalize_normals()
    pcd.orient_normals_consistent_tangent_plane(50)

    return pcd


def poisson_mesh(pcd, depth=8):
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        pcd,
        depth=depth
    )

    densities = np.asarray(densities)

    if len(densities) > 0:
        mask = densities > np.quantile(densities, 0.05)
        mesh.remove_vertices_by_mask(~mask)

    mesh.compute_vertex_normals()
    mesh.compute_triangle_normals()
    mesh.orient_triangles()

    return mesh


def run_pipeline(input_path="data/global_cloud.ply"):
    pcd = load_pointcloud(input_path)

    if len(pcd.points) < 100:
        raise ValueError("Point cloud too small: fusion likely failed")

    pcd = clean_pointcloud(pcd)

    pcd = estimate_normals(pcd)

    mesh = poisson_mesh(pcd)

    if len(mesh.vertices) == 0:
        raise ValueError("Mesh generation failed")

    o3d.io.write_triangle_mesh("data/mesh.ply", mesh)
    o3d.io.write_point_cloud("data/clean_cloud.ply", pcd)

    print("Mesh saved: data/mesh.ply")

    try:
        o3d.visualization.draw_geometries(
            [mesh],
            mesh_show_back_face=True
        )
    except:
        print("Visualization skipped")


if __name__ == "__main__":
    run_pipeline()