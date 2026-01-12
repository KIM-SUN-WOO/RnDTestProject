import numpy as np
def angle_v2(vec1, vec2):
    #compute angle between 2 vectors. ... from google

    # 각 벡터의 각도 계산 (x축 기준)
    angle1 = np.arctan2(vec1[:,1], vec1[:,0])
    angle2 = np.arctan2(vec2[:,1], vec2[:,0])

    # 두 각도의 차이 계산
    angle_diff_rad = angle2 - angle1

    # 절대값 및 360도 조정 (필요에 따라)
    angle_diff_deg = np.degrees(angle_diff_rad)
    #angle_diff_deg = np.where( angle_diff_deg < 0, angle_diff_deg + 360, angle_diff_deg )

    return angle_diff_deg
