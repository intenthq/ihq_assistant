## Reasons to use an open-source (or open-access) language model

- Local deployment to guarantee data privacy
- Possibility of fine tuning on labeled data sets
- Potentially lower costs

## Things to consider when choosing a model for deployment

- Technical requirements
  - Possibility of running on CPU vs GPU (or hybrid)
  - Size of the model and memory requirements
- Available model sizes and existence of *quantised* models
  - Quantised models have reduced weight precision (e.g. using a 5 bit integer instead of the original 16 bit float to represent weight values)
  - These models can offer a good compromise between model size and performance. Smaller model size means lower memory requirements which can reduce the cost significantly, especially when running on GPUs
- Licence details, ease of access
- Task performance
  - Hard to establish without trying it out
  - Existence of fine tuned versions

# Available models

| Name | Summary | Access | Model versions | Resources required | Performance |
| --- | --- | --- | --- | --- | --- |
| Llama 2 | Created by Meta (Facebook) on a custom Llama 2 dataset<br/>Pros: Easy to deploy on CPU/GPU, very popular in the community with many fine-tuned and quantised versions and many tutorials available, seems quite performant<br/>Cons: Not quite open source and requires Meta permission (at least for the original model weights) | Model architecture and weights released as **open-access** (not technically open source) under a custom [Llama 2 Licence](https://github.com/facebookresearch/llama/blob/main/LICENSE)<br/>The licence allows for commercial and non-commercial use, with one exception; any company with a product with 700M active users in the month preceding Llama 2 release must request special permission. That does not seem to apply to us, so we should be fine<br/>To access the model weights published by Meta (for the original base or fine-tuned models), one has to [fill out a form on their website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and get approval first<br/>If downloading the model files from [Hugging Face](https://huggingface.co/meta-llama), the email given in the form must be the same as the one used for account creation on Hugging Face<br/>On the other hand there are many derivative models available, e.g. quantised versions published by user [TheBloke](https://huggingface.co/TheBloke) ([e.g. this one](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF)) - these can be downloaded directly, without any forms. It’s possible that approval by Meta is still technically required for lawful use (in any case, the original licence still applies) | Meta published two model versions in three sizes (for 6 models total)<br/>Base version with no fine-tuning and a *chat* version tuned with human feedback for dialog and instruction use cases<br/>The model sizes are: 7B (billion parameters), 13B and 70B<br/>[The model files are available on Hugging Face](https://huggingface.co/meta-llama)<br/>There are many derivative versions of the model available on Hugging Face<br/>In particular, user TheBloke [publishes the original and modified models](https://huggingface.co/TheBloke?search_models=llama-2) in quantised versions<br/>The quantised versions are available in formats compatible with the GGML library, allowing for efficient running on CPU and GPU | The original models available on Hugging Face are in PyTorch format, easy to run with the [transformers package](https://huggingface.co/docs/transformers/index)<br/>These are apparently much faster to run on GPUs<br/>There are open-source tools available for running the original and quantised models on CPUs (or mix of CPU/GPU)<br/>These are the [GGML library](https://github.com/ggerganov/ggml), [llama.cpp](https://github.com/ggerganov/llama.cpp) tool and [ctransformers package](https://github.com/marella/ctransformers) for python integration<br/>These tools are particularly useful for running locally on Apple computers with M1/2 Apple Silicon chips but could be useful when deploying on the cloud too | This is very hard to assess at this stage but I was able to deploy the 13B-chat version (quantised) locally on my laptop and prompt it to return valid JSON files with an ElasticSearch query corresponding to a simple audience description<br/>The model seems capable enough for early experimentation, and the 70B version should be even better |
| Falcon | The Falcon is an open-source model developed by the [Technology Innovation Institute](https://www.tii.ae/) in Abu Dhabi<br/>It’s trained on a specially curated dataset called [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)<br/>Apparently quite performant but likely to require very expensive resources to run | The model architecture and weights are released under the Apache 2.0 licence, making it truly open-source and ok to use for commercial and non-commercial purposes<br/>[Available on Hugging Face](https://huggingface.co/tiiuae) without any access restrictions | TII published three model sizes and two versions at each size<br/>The model sizes are 7B (billion parameters), 40B and the newest 180B<br/>The 7B and 40B models have a base version and an “instruct” version fine-tuned to respond to instructions<br/>The 180B model has a base version and a fine-tuned “chat” version<br/>The fine-tuning dataset is different than for the smaller models, but I’m not sure what the objective difference is between “chat” and “instruct”<br/>[Model files on Hugging Face](https://huggingface.co/tiiuae)<br/>There are some quantised versions available and a number of additionally tuned ones on Hugging Face<br/>[TODO: Post links] | The models are quite large, especially the 40B and 180B ones, and there are not many quantised versions easily available<br/>It seems like they have to be run on GPUs to operate efficiently, which would impose quite high cost | The authors claim the 180B model outperforms LLama 2 70B and GPT-3.5 at standard language benchmarks<br/>There is a [public demo environment available](https://huggingface.co/spaces/tiiuae/falcon-180b-demo), and while playing with it I was able to get very similar performance to the locally deployed Llama 2 13B (quantised) out of the box; it’s hard to assess if the model would outperform the bigger Llama model with well structured prompts |
| MPT |  |  |  |  |  |


## Llama 2

- Created by Meta (Facebook) on a custom Llama 2 dataset

### Access

- Model architecture and weights released as **open-access** (not technically open source) under a custom [Llama 2 Licence](https://github.com/facebookresearch/llama/blob/main/LICENSE)
- The licence allows for commercial and non-commercial use, with one exception; any company with a product with 700M active users in the month preceding Llama 2 release must request special permission. That does not seem to apply to us, so we should be fine
- To access the model weights published by Meta (for the original base or fine-tuned models), one has to [fill out a form on their website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and get approval first
  - If downloading the model files from [Hugging Face](https://huggingface.co/meta-llama), the email given in the form must be the same as the one used for account creation on Hugging Face
  - On the other hand there are many derivative models available, e.g. quantised versions published by user [TheBloke](https://huggingface.co/TheBloke) ([e.g. this one](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF)) - these can be downloaded directly, without any forms. It’s possible that approval by Meta is still technically required for lawful use (in any case, the original licence still applies)

### Model versions

- Meta published two model versions in three sizes (for 6 models total)
  - Base version with no fine-tuning and a *chat* version tuned with human feedback for dialog and instruction use cases
  - The model sizes are: 7B (billion parameters), 13B and 70B
  - [The model files are available on Hugging Face](https://huggingface.co/meta-llama)
- There are many derivative versions of the model available on Hugging Face
  - In particular, user TheBloke [publishes the original and modified models](https://huggingface.co/TheBloke?search_models=llama-2) in quantised versions
  - The quantised versions are available in formats compatible with the GGML library, allowing for efficient running on CPU and GPU

### Resources required

- The original models available on Hugging Face are in PyTorch format, easy to run with the [transformers package](https://huggingface.co/docs/transformers/index)
  - These are apparently much faster to run on GPUs
- There are open-source tools available for running the original and quantised models on CPUs (or mix of CPU/GPU)
  - These are the [GGML library](https://github.com/ggerganov/ggml), [llama.cpp](https://github.com/ggerganov/llama.cpp) tool and [ctransformers package](https://github.com/marella/ctransformers) for python integration
  - These tools are particularly useful for running locally on Apple computers with M1/2 Apple Silicon chips but could be useful when deploying on the cloud too

### Performance

- This is very hard to assess at this stage but I was able to deploy the 13B-chat version (quantised) locally on my laptop and prompt it to return valid JSON files with an ElasticSearch query corresponding to a simple audience description
- The model seems capable enough for early experimentation, and the 70B version should be even better

### Summary

- Pros: Easy to deploy on CPU/GPU, very popular in the community with many fine-tuned and quantised versions and many tutorials available, seems quite performant
- Cons: Not quite open source and requires Meta permission (at least for the original model weights)

## Falcon

- The Falcon is an open-source model developed by the [Technology Innovation Institute](https://www.tii.ae/) in Abu Dhabi
- It’s trained on a specially curated dataset called [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)

### Access

- The model architecture and weights are released under the Apache 2.0 licence, making it truly open-source and ok to use for commercial and non-commercial purposes

##