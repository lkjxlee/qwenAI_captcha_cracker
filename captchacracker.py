import base64
import dashscope

def captchacracker(image_base64_data,api_key):
    dashscope.api_key = api_key
    response = dashscope.MultiModalConversation.call(
        model='qwen-vl-max',
        messages=[
            {
                'role': 'user',
                'content': [
                    {'text': '请告诉我这张图中的数字或字母内容,直接输出就行,不要任何空格和标点符号'},                           #根据需要调整，比如数字,汉字，数学计算
                    {'image': f'data:image/png;base64,{image_base64_data}'}                                       #DashScope 格式
                ]
            }
        ]
    )

    return response.output.choices[0].message.content[0]['text']


