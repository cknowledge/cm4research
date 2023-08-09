# Taken from https://github.com/finegrain-ai/refiners
# LICENSE: MIT

import os

if __name__ == "__main__":

    from refiners.foundationals.latent_diffusion import StableDiffusion_1
    from refiners.foundationals.latent_diffusion.lora import LoraWeights
    from refiners.fluxion.utils import load_from_safetensors, manual_seed
    import torch

    sd15 = StableDiffusion_1(device="cuda")
    sd15.clip_text_encoder.load_state_dict(load_from_safetensors("CLIPTextEncoderL.safetensors"))
    sd15.lda.load_state_dict(load_from_safetensors("lda.safetensors"))
    sd15.unet.load_state_dict(load_from_safetensors("unet.safetensors"))

    # This uses the LoraAdapter internally and takes care to inject it where it should
    lora_weights = LoraWeights("pokemon_lora.safetensors", device=sd15.device)
    lora_weights.patch(sd15, scale=1.0)

    x=os.environ.get('CM_REFINERS_PROMPT','')
    prompt = "a cute cat" if x=='' else x

    with torch.no_grad():
        clip_text_embedding = sd15.compute_text_embedding(prompt)

    sd15.set_num_inference_steps(30)

    manual_seed(2)
    x = torch.randn(1, 4, 64, 64, device=sd15.device)

    output=os.environ['CM_REFINERS_OUTPUT_FILE']

    with torch.no_grad():
        for step in sd15.steps:
            x = sd15(
                x,
                step=step,
                clip_text_embedding=clip_text_embedding,
                condition_scale=7.5,
            )
        predicted_image = sd15.lda.decode_latents(x)
        predicted_image.save(output)

    exit(0)