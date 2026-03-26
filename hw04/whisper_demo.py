import whisper

# 加载轻量版模型（适合笔记本，速度快）
model = whisper.load_model("base")

# 识别当前目录下的 test.wav 音频（中文）
print("🔍 正在识别音频...")
result = model.transcribe("test.wav", language="zh")

# 输出识别结果
print("\n✅ 识别完成：")
print(result["text"])