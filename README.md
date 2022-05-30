# qa-text-source-comparison

This repository contains the data and crowdsourcing instructions used in [*What Makes Reading Comprehension Questions Difficult?* (Sugawara et al., ACL 2022)](https://aclanthology.org/2022.acl-long.479/).

## Contents

- `data` contains all collected data in our study.
  + The questions written for passages taken from MCTest, RACE, and ReClor are missing their passages because of its license. Refer to the `collect missing passage` section to get the complete data.
- `crowdsourcing_templates` contains the html templates of task and instructions used in crowdsourcing.
  + We used this [crowdsourcing tool](https://github.com/nyu-mll/crowdsourcing-protocol-comparison) that was developed in our previous study.
  + To view the instructions etc on the web browser, put these files under `web/templates` and modify a config file.

## Complete Missing Passages

First, download the raw datasets from the following links:

- MCTest: https://mattr1.github.io/mctest/data.html
- RACE: https://www.cs.cmu.edu/~glai1/data/race/
- ReClor: https://whyu.me/reclor/#download

Make sure to put data such that:

- `data/mctest/mc{160,500}.train.tsv`
- `data/race/train/{middle,high}/*.txt`
- `data/reclor/train.json`

Then run:

```
python data/collect_missing_passages.py
```

You will get `data/complete_data.json` for the complete data.


## Data Overview

- `passage`, `question`, `options`: question data
- `question_id`: `{source}_{plain,adv}`
  + `plain` is standard data collection and `adv` is adversarial data collection
- `passage_id`: unique id for identifying the source passage
- `gold_label`: zero-indexed answer index (0-3) among four options
- `worker_id`: anonymized worker id
- `elapsed_time_second`: writing time
- `source`: passage source
  + MCTest
  + RACE
  + Project Gutenberg
  + Open ANC (Slate section)
  + ReClor
  + Wikipedia arts articles
  + Wikipedia science articles
- `validation_data`
  + `worker_answer_index`: zero-indexed answer index
  + `correct`: validator's answer matches the gold label or not
  + `elapsed_time_second`: answering time for five questions (in a single HIT; not averaged)
  + `unanswerable`: if being unanswerable option is flagged or not
  + `worker_id`: anonymized worker id
- `model_predictions` and `model_predictions-partial`
  + a list of pairs of [`model_name`, `if_model_gets_correct_or_not`]
  + `A`: only options are given
  + `P+A`: only passage and options are given
  + `Q+A`: only question and options are given
- `validation_index_for_filtering`:  which validation votes are used for validation
  + A question is validated if at least one of two labels is equal to the gold label
- `validation_index_for_performance`:  which validation votes are used for computing human accuracy
- `valid`: True if a question is validated
- `unanimous`: True if both two filtering labels are equal to the gold label
- `human_accuracy`: human accuracy
- `model_accuracy`: average model accuracy of eight models (excluding Unified QA)
- `human_model_gap`: `human_accuracy` - `model_accuracy`
- `question_type`: interrogative word-based question type
- `difficulty`: {`easy`, `mid`, `hard`} (Refer to the paper for the definition)
- `reasoning_types`: Some questions have annotation results.
- `readability`: values of readability measures.

For the questions collected with model-in-the-loop, there are the following values:

- `adversarial_model_prediction_probability`
- `adversarial_model_prediction_label`
- `num_of_adv_submission`: how many times a worker makes submission for fooling the adversarial model (UnifiedQA large)
- `adversarial_success`: True if a worker fools the model


## License

The collected questions and options (excluding passages) are released under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0).


## Citation

```
@inproceedings{sugawara-etal-2022-makes,
  title={What Makes Reading Comprehension Questions Difficult?},
  author={Saku Sugawara, Nikita Nangia, Alex Warstadt, Samuel R. Bowman},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},
  month=may,
  year={2022},
  address = {Online and Dublin, Ireland},
  publisher = {Association for Computational Linguistics},
}
```
