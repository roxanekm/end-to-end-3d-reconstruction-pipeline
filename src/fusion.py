import open3d as o3d

def fuse_pointclouds(pcd_list):
    if len(pcd_list) == 0:
        return None

    global_pcd = pcd_list[0]

    for pcd in pcd_list[1:]:
        global_pcd += pcd

    global_pcd = global_pcd.voxel_down_sample(voxel_size=0.01)

    global_pcd, _ = global_pcd.remove_statistical_outlier(
        nb_neighbors=20,
        std_ratio=2.0
    )

    return global_pcd