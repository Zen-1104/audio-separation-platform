from huggingface_hub import HfApi

api = HfApi()
api.upload_folder(
    folder_path = "backend",
    repo_id = "Zen-4011/audio-separation-model",
    token = "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",
    repo_type = "space",
)
print("Deployed to Hugging Face.")