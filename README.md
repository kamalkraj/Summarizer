# Summarizer

## Requirements

- python3
- cuda 10.0 (optional) 

## Setup

```
- pip install -r requirements.txt
- wget https://dl.fbaipublicfiles.com/fairseq/models/bart.large.cnn.tar.gz
- tar -xf bart.large.cnn.tar.gz
```


## Run

```
python api.py
```


# REST API

```bash
curl -X POST http://0.0.0.0:8888/summarize \
    -H 'Content-Type: application/json' \
    -d '{"document": "If you travel by plane and arriving on time makes a difference, try to book on Hawaiian Airlines. In 2012, passengers got where they needed to go without delay on the carrier more than nine times out of 10, according to a study released on Monday.In fact, Hawaiian got even better from 2011, when it had a 92.8% on-time performance. Last year, it improved to 93.4%."}'  
```
Result
```json
{
    "summary": "In 2012, passengers got where they needed to go without delay on the carrier more than nine times out of 10. In 2011, Hawaiian got even better from 2011, when it had a 92.8% on-time performance. Last year, it improved to 93.4%."
}
```