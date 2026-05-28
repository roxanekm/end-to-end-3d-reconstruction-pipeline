import numpy as np
import open3d as o3d

def depth_to_pointcloud(depth, image, fx=500, fy=500, stride=4):
    h, w = depth.shape

    xs, ys = np.meshgrid(
        np.arange(0, w, stride),
        np.arange(0, h, stride)
    )

    zs = depth[::stride, ::stride]

    mask = zs > 0

    xs = xs[mask]
    ys = ys[mask]
    zs = zs[mask]

    X = (xs - w / 2) * zs / fx
    Y = -(ys - h / 2) * zs / fy
    Z = zs

    points = np.stack((X, Y, Z), axis=-1)

    colors = image[ys, xs] / 255.0

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points.astype(np.float64))
    pcd.colors = o3d.utility.Vector3dVector(colors.astype(np.float64))

    return pcd