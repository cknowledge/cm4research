# Reproducibility report automated by CM

We are trying to run the [Refiners "Hello World" example](https://github.com/finegrain-ai/refiners#getting-started).

It currently fails with the following settings:
* OS: Ubuntu 22.04.2 LTS
* Python: 3.10.12
* CUDA 11.5 and 11.8
* PyTorch CUDA 2.0.0 and 2.0.1
* Refiners from PYPI: 0.1.0

Steps to reproduce:

Install [CM automation language](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull main repository with CM automation recipes for AI/ML systems:
```bash
cm pull repo mlcommons@ck
```

Pull this repository with reproducibility reports automated by CM:
```bash
cm pull repo cknowledge@cm-reproduce
```

Install Python virtual env via CM:
```bash
cmr "install python-venv" --name=refiners --version_min=3.10.1
```

Tested with CUDA 11.8.0 and PyTorch 2.0.1

Get CUDA 11.8.0 via CM:
```bash
cmr "get cuda" --version=11.8.0
```

Get PyTorch CUDA 2.0.1:
```bash
cmr "get generic-python-lib _torch_cuda" --version=2.0.1
```

Get Refiners Python library 0.0.1:
```bash
cmr "get generic-python-lib _package.refiners" --version=0.1.0
```


Run refiner's "Hello World" example:
```bash
cmr "run python-app refiners hello-world _cuda" --adr.python.name=refiners
```

# Log

It fails at the moment with the following log:
```bash
python scripts/convert-lora-weights.py --from pytorch_lora_weights.bin --output-file pokemon_lora.safetensors

Loading pipeline components...:  29%|██████████████████████████████████▊                                                                                       | 2/7 [00:00<00:00, 10.85it/s]`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["id2label"]` will be overriden.
`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["bos_token_id"]` will be overriden.
`text_config_dict` is provided which will be used to initialize `CLIPTextConfig`. The value `text_config["eos_token_id"]` will be overriden.
Loading pipeline components...: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:01<00:00,  5.05it/s]
('Conv2d', (torch.Size([640, 320, 3, 3]), torch.Size([640])))
        DownBlocks.Chain_5.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
('Conv2d', (torch.Size([1280, 1280, 1, 1]), torch.Size([1280])))
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_1.Conv2d        ---
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_3.Conv2d        ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
('Conv2d', (torch.Size([320, 640, 3, 3]), torch.Size([320])))
        UpBlocks.Chain_11.ResidualBlock.Chain.RangeAdapter2d.Conv2d     ---
        UpBlocks.Chain_12.ResidualBlock.Chain.RangeAdapter2d.Conv2d     ---
('Linear', (torch.Size([640, 1280]), torch.Size([640])))
        DownBlocks.Chain_5.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      ---
        DownBlocks.Chain_6.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      ---
        UpBlocks.Chain_7.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_8.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_9.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
('Conv2d', (torch.Size([640, 960, 3, 3]), torch.Size([640])))
        UpBlocks.Chain_9.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
('Linear', (torch.Size([2560, 320]), torch.Size([2560])))
        DownBlocks.Chain_2.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        DownBlocks.Chain_3.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        UpBlocks.Chain_10.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1    ---
        UpBlocks.Chain_11.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1    ---
        UpBlocks.Chain_12.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1    ---
('Conv2d', (torch.Size([1280, 640, 3, 3]), torch.Size([1280])))
        DownBlocks.Chain_8.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
('Conv2d', (torch.Size([320, 640, 1, 1]), torch.Size([320])))
        UpBlocks.Chain_11.ResidualBlock.Conv2d  ---
        UpBlocks.Chain_12.ResidualBlock.Conv2d  ---
('Conv2d', (torch.Size([1280, 2560, 3, 3]), torch.Size([1280])))
        UpBlocks.Chain_1.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
        UpBlocks.Chain_2.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
        UpBlocks.Chain_3.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
        UpBlocks.Chain_4.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
        UpBlocks.Chain_5.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
('Conv2d', (torch.Size([640, 960, 1, 1]), torch.Size([640])))
        UpBlocks.Chain_9.ResidualBlock.Conv2d   ---
('Conv2d', (torch.Size([640, 640, 3, 3]), torch.Size([640])))
        DownBlocks.Chain_5.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_6.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
        DownBlocks.Chain_6.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_7.Downsample.Conv2d    ---
        UpBlocks.Chain_7.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_8.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_9.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_9.Upsample.Conv2d        ---
('Conv2d', (torch.Size([640, 320, 1, 1]), torch.Size([640])))
        DownBlocks.Chain_5.ResidualBlock.Conv2d ---
('Conv2d', (torch.Size([640, 1920, 1, 1]), torch.Size([640])))
        UpBlocks.Chain_7.ResidualBlock.Conv2d   ---
('Conv2d', (torch.Size([640, 1920, 3, 3]), torch.Size([640])))
        UpBlocks.Chain_7.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
('Conv2d', (torch.Size([640, 1280, 3, 3]), torch.Size([640])))
        UpBlocks.Chain_8.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
('Linear', (torch.Size([1280, 1280]), torch.Size([1280])))
        TimestepEncoder.RangeEncoder.Linear_2   time_embedding.linear_2
        DownBlocks.Chain_8.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      down_blocks.2.attentions.0.transformer_blocks.0.attn1.to_out.0
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear       down_blocks.2.attentions.0.transformer_blocks.0.attn2.to_out.0
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear   down_blocks.2.attentions.1.transformer_blocks.0.attn1.to_out.0
        DownBlocks.Chain_9.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      down_blocks.2.attentions.1.transformer_blocks.0.attn2.to_out.0
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear       mid_block.attentions.0.transformer_blocks.0.attn1.to_out.0
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear   mid_block.attentions.0.transformer_blocks.0.attn2.to_out.0
        DownBlocks.Chain_11.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear     up_blocks.1.attentions.0.transformer_blocks.0.attn1.to_out.0
        DownBlocks.Chain_12.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear     up_blocks.1.attentions.0.transformer_blocks.0.attn2.to_out.0
        Sum.MiddleBlock.ResidualBlock_1.Chain.RangeAdapter2d.Chain.Linear       up_blocks.1.attentions.1.transformer_blocks.0.attn1.to_out.0
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear  up_blocks.1.attentions.1.transformer_blocks.0.attn2.to_out.0
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear      up_blocks.1.attentions.2.transformer_blocks.0.attn1.to_out.0
        Sum.MiddleBlock.ResidualBlock_2.Chain.RangeAdapter2d.Chain.Linear       up_blocks.1.attentions.2.transformer_blocks.0.attn2.to_out.0
        UpBlocks.Chain_1.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_2.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_3.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_4.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear     ---
        UpBlocks.Chain_5.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear     ---
        UpBlocks.Chain_6.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear        ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_1.Chain.SelfAttention.Linear ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_2.Chain.Attention.Linear     ---
('Conv2d', (torch.Size([640, 640, 1, 1]), torch.Size([640])))
        DownBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        DownBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        UpBlocks.Chain_7.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_7.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
        UpBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
        UpBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_1.Conv2d       ---
        UpBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_3.Conv2d       ---
('Conv2d', (torch.Size([320, 320, 1, 1]), torch.Size([320])))
        DownBlocks.Chain_2.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_2.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        DownBlocks.Chain_3.CLIPLCrossAttention.Chain.Chain_1.Conv2d     ---
        DownBlocks.Chain_3.CLIPLCrossAttention.Chain.Chain_3.Conv2d     ---
        UpBlocks.Chain_10.CLIPLCrossAttention.Chain.Chain_1.Conv2d      ---
        UpBlocks.Chain_10.CLIPLCrossAttention.Chain.Chain_3.Conv2d      ---
        UpBlocks.Chain_11.CLIPLCrossAttention.Chain.Chain_1.Conv2d      ---
        UpBlocks.Chain_11.CLIPLCrossAttention.Chain.Chain_3.Conv2d      ---
        UpBlocks.Chain_12.CLIPLCrossAttention.Chain.Chain_1.Conv2d      ---
        UpBlocks.Chain_12.CLIPLCrossAttention.Chain.Chain_3.Conv2d      ---
('Linear', (torch.Size([5120, 640]), torch.Size([5120])))
        DownBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        DownBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        UpBlocks.Chain_7.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
        UpBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
        UpBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
('Linear', (torch.Size([640, 2560]), torch.Size([640])))
        DownBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        DownBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        UpBlocks.Chain_7.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
        UpBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
        UpBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
('Conv2d', (torch.Size([1280, 1920, 3, 3]), torch.Size([1280])))
        UpBlocks.Chain_6.ResidualBlock.Chain.RangeAdapter2d.Conv2d      ---
('Linear', (torch.Size([10240, 1280]), torch.Size([10240])))
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1   ---
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1      ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_1     ---
('Conv2d', (torch.Size([1280, 2560, 1, 1]), torch.Size([1280])))
        UpBlocks.Chain_1.ResidualBlock.Conv2d   ---
        UpBlocks.Chain_2.ResidualBlock.Conv2d   ---
        UpBlocks.Chain_3.ResidualBlock.Conv2d   ---
        UpBlocks.Chain_4.ResidualBlock.Conv2d   ---
        UpBlocks.Chain_5.ResidualBlock.Conv2d   ---
('Linear', (torch.Size([1280, 5120]), torch.Size([1280])))
        DownBlocks.Chain_8.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        DownBlocks.Chain_9.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        Sum.MiddleBlock.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2      ---
        UpBlocks.Chain_4.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
        UpBlocks.Chain_5.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
        UpBlocks.Chain_6.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2     ---
('Conv2d', (torch.Size([640, 1280, 1, 1]), torch.Size([640])))
        UpBlocks.Chain_8.ResidualBlock.Conv2d   ---
('Conv2d', (torch.Size([320, 960, 1, 1]), torch.Size([320])))
        UpBlocks.Chain_10.ResidualBlock.Conv2d  ---
('Conv2d', (torch.Size([1280, 640, 1, 1]), torch.Size([1280])))
        DownBlocks.Chain_8.ResidualBlock.Conv2d ---
('Conv2d', (torch.Size([1280, 1280, 3, 3]), torch.Size([1280])))
        DownBlocks.Chain_8.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_9.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
        DownBlocks.Chain_9.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_10.Downsample.Conv2d   ---
        DownBlocks.Chain_11.ResidualBlock.Chain.RangeAdapter2d.Conv2d   ---
        DownBlocks.Chain_11.ResidualBlock.Chain.Conv2d  ---
        DownBlocks.Chain_12.ResidualBlock.Chain.RangeAdapter2d.Conv2d   ---
        DownBlocks.Chain_12.ResidualBlock.Chain.Conv2d  ---
        Sum.MiddleBlock.ResidualBlock_1.Chain.RangeAdapter2d.Conv2d     ---
        Sum.MiddleBlock.ResidualBlock_1.Chain.Conv2d    ---
        Sum.MiddleBlock.ResidualBlock_2.Chain.RangeAdapter2d.Conv2d     ---
        Sum.MiddleBlock.ResidualBlock_2.Chain.Conv2d    ---
        UpBlocks.Chain_1.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_2.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_3.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_3.Upsample.Conv2d        ---
        UpBlocks.Chain_4.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_5.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_6.ResidualBlock.Chain.Conv2d     ---
        UpBlocks.Chain_6.Upsample.Conv2d        ---
('Conv2d', (torch.Size([320, 960, 3, 3]), torch.Size([320])))
        UpBlocks.Chain_10.ResidualBlock.Chain.RangeAdapter2d.Conv2d     ---
('Conv2d', (torch.Size([320, 320, 3, 3]), torch.Size([320])))
        DownBlocks.Chain_2.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
        DownBlocks.Chain_2.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_3.ResidualBlock.Chain.RangeAdapter2d.Conv2d    ---
        DownBlocks.Chain_3.ResidualBlock.Chain.Conv2d   ---
        DownBlocks.Chain_4.Downsample.Conv2d    ---
        UpBlocks.Chain_10.ResidualBlock.Chain.Conv2d    ---
        UpBlocks.Chain_11.ResidualBlock.Chain.Conv2d    ---
        UpBlocks.Chain_12.ResidualBlock.Chain.Conv2d    ---
('Conv2d', (torch.Size([1280, 1920, 1, 1]), torch.Size([1280])))
        UpBlocks.Chain_6.ResidualBlock.Conv2d   ---
('Linear', (torch.Size([320, 1280]), torch.Size([320])))
        DownBlocks.Chain_2.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      ---
        DownBlocks.Chain_2.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        DownBlocks.Chain_3.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear      ---
        DownBlocks.Chain_3.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2   ---
        UpBlocks.Chain_10.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear       ---
        UpBlocks.Chain_10.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2    ---
        UpBlocks.Chain_11.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear       ---
        UpBlocks.Chain_11.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2    ---
        UpBlocks.Chain_12.ResidualBlock.Chain.RangeAdapter2d.Chain.Linear       ---
        UpBlocks.Chain_12.CLIPLCrossAttention.Chain.Chain_2.CrossAttentionBlock.Sum_3.Chain.Linear_2    ---
Traceback (most recent call last):
  File "/home/ubuntu/CM/repos/local/cache/5b856b1e828c441f/repo/scripts/convert-lora-weights.py", line 115, in <module>
    main()
  File "/home/ubuntu/CM/repos/local/cache/5b856b1e828c441f/repo/scripts/convert-lora-weights.py", line 111, in main
    process(source=args.source, base_model=args.base_model, output_file=args.output_file)
  File "/home/ubuntu/CM/repos/local/cache/18b76cf0624a490c/refiners/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/CM/repos/local/cache/5b856b1e828c441f/repo/scripts/convert-lora-weights.py", line 57, in process
    assert diffusers_to_refiners
AssertionError
```
