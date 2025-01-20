

## Preservation of pre-trained models

If the particular paper tunes a model, it can also be made available through Hugging Face, and a DOI requested. Alternatively, models and or datasets can be preserved on Zenodo or some other repository that allows for large objects to be stored.


Datasets that are used to train LLMs can also be made available through the same repositories.

## Citing models and datasets

Many LLMs are made available through the [Hugging Face Model Hub](https://huggingface.co/), and are either used directly or through Python packages, e.g. [SentenceTransformer](https://www.sbert.net/docs/package_reference/sentence_transformer). 


- The input parameters for the LLM models (pulled from Huggingface) should be precisely specified (URL) and cited (using DOI if available). For instance, there are 540 models with `sbert`  in the name. The original `BERT` model is on Google Drive (<https://github.com/google-research/bert/tree/master>). Please be precise about which one you used, and when you last accessed it (as in theory, they might change).


### Model without DOI:

```
@techreport {all-distilrobert-v1,
	author       = { {Sentence Transformers} },
	title        = { sentence-transformers/all-distilroberta-v1 },
	year         = 2024,
	url          = { https://huggingface.co/sentence-transformers/all-distilroberta-v1 },
	institution    = { Hugging Face },
  type         = { Model },
  number       = { 8d88b92 },
}
```

### Dataset with DOI:

```
@misc {dell_research_harvard_2023,
	author       = { {Dell Research Harvard} },
	title        = { AmericanStories (Revision 3484aca) },
	year         = 2023,
	url          = { https://huggingface.co/datasets/dell-research-harvard/AmericanStories },
	doi          = { 10.57967/hf/0757 },
	publisher    = { Hugging Face }
}
```

When a [DOI is available](https://huggingface.co/docs/hub/en/doi), which can only be requested by the owner of the model or dataset, then it should be used instead.


Please be sure to also provide the exact version of the Python packages used (e.g., `SentenceTransformer`), so that any default parameters are clearly identifiable, should they change across versions.
