# palm-detection

Based on mediapipe. 

Modify the outputs in : `xxx/mediapipe/python/solutions/hands`:
<br />
`
        Hands.__init__() -> outputs=[
            'multi_hand_landmarks', 'multi_hand_world_landmarks',
            'multi_handedness','palm_detections'
        ])
        `

![example](https://github.com/luohwu/palm-detection/blob/main/sample.png)
