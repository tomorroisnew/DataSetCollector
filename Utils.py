import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#FUNCTION TO extract LandMarks GESTURES
def extractLandMarks(hand_landmarks):
    center_x = (hand_landmarks.landmark[0].x + hand_landmarks.landmark[5].x + hand_landmarks.landmark[17].x)/3
    center_y = (hand_landmarks.landmark[0].y + hand_landmarks.landmark[5].y + hand_landmarks.landmark[17].y)/3
    center_z = (hand_landmarks.landmark[0].z + hand_landmarks.landmark[5].z + hand_landmarks.landmark[17].z)/3
    
    thumb_tip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    thumb_tip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    thumb_tip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z
    thumb_ip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    thumb_ip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
    thumb_ip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].z
    thumb_mcp_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
    thumb_mcp_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    thumb_mcp_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].z
    thumb_cmc_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
    thumb_cmc_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
    thumb_cmc_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].z

    index_tip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
    index_tip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    index_tip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
    index_dip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
    index_dip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
    index_dip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].z
    index_pip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
    index_pip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    index_pip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].z
    index_mcp_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
    index_mcp_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    index_mcp_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].z
    
    middle_tip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
    middle_tip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    middle_tip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
    middle_dip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
    middle_dip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
    middle_dip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z
    middle_pip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
    middle_pip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    middle_pip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z
    middle_mcp_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
    middle_mcp_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    middle_mcp_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
    
    ring_tip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
    ring_tip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    ring_tip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
    ring_dip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
    ring_dip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
    ring_dip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].z
    ring_pip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
    ring_pip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    ring_pip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].z
    ring_mcp_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
    ring_mcp_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    ring_mcp_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    
    pinky_tip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x
    pinky_tip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
    pinky_tip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z
    pinky_dip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x
    pinky_dip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
    pinky_dip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].z
    pinky_pip_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
    pinky_pip_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
    pinky_pip_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].z
    pinky_mcp_x = center_x - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
    pinky_mcp_y = center_y - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
    pinky_mcp_z = center_z - hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].z

    d1_x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
    d1_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    d1_z = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z - hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
    d2_x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
    d2_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    d2_z = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z - hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z
    d3_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
    d3_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    d3_z = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z - hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z
    d4_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    d4_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    d4_z = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z - hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z

    #data to be saved
    data = np.array([center_x, center_y, center_z, thumb_tip_x, thumb_tip_y, thumb_tip_z, thumb_ip_x, thumb_ip_y, thumb_ip_z, thumb_mcp_x, thumb_mcp_y, thumb_mcp_z, thumb_cmc_x, thumb_cmc_y, thumb_cmc_z, index_tip_x, index_tip_y, index_tip_z, index_dip_x, index_dip_y, index_dip_z, index_pip_x, index_pip_y, index_pip_z, index_mcp_x, index_mcp_y, index_mcp_z, middle_tip_x, middle_tip_y, middle_tip_z, middle_dip_x, middle_dip_y, middle_dip_z, middle_pip_x, middle_pip_y, middle_pip_z, middle_mcp_x, middle_mcp_y, middle_mcp_z, ring_tip_x, ring_tip_y, ring_tip_z, ring_dip_x, ring_dip_y, ring_dip_z, ring_pip_x, ring_pip_y, ring_pip_z, ring_mcp_x, ring_mcp_y, ring_mcp_z, pinky_tip_x, pinky_tip_y, pinky_tip_z, pinky_dip_x, pinky_dip_y, pinky_dip_z, pinky_pip_x, pinky_pip_y, pinky_pip_z, pinky_mcp_x, pinky_mcp_y, pinky_mcp_z, d1_x, d1_y, d1_z, d2_x, d2_y, d2_z, d3_x, d3_y, d3_z, d4_x, d4_y, d4_z])

    return data