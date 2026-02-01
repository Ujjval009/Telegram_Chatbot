from dotenv import load_dotenv
import os
import sys
from aiogram import Bot, Dispatcher , types ,  executor
from aiogram.utils import executor 
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype=torch.float16,
    load_in_4bit=True
)

def generate_response(user_message: str) -> str:
    prompt = f"""<s>[INST] {user_message} [/INST]"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.replace(prompt, "").strip()