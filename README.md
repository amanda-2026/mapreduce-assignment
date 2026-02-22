# MapReduce Assignment 2 – Harry Potter Word Analysis
> This is intended for reproduction in a **Linux environment**. 
## Overview
This project analyzes text from selected Harry Potter book pages using **Hadoop Streaming and Python MapReduce scripts**.  

There are two tasks:
1. Count occurrences of each word in `file1.txt`.
2. Count occurrences of non-English words (names, places, spells, etc.) in `file2.txt` using `pyspellchecker`.

The scripts are designed to run in **Hadoop local mode**, so no HDFS setup or SSH configuration is required.

---

## Dependencies
- Python 3.x  
- pyspellchecker (`pip install pyspellchecker`)  
- Hadoop 3.3.x

---

## How to Run

### 1. Prepare output folders
Hadoop cannot overwrite existing output directories. Delete them first if they exist:

```bash
rm -rf output/output_wordcount
rm -rf output/output_nonenglish
```
### 2. Run word count
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input input/file1.txt \
  -output output/output_wordcount \
  -mapper scripts/mapper.py \
  -reducer scripts/reducer.py
  ```
### 3. Run Non-English words
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input input/file2.txt \
  -output output/output_nonenglish \
  -mapper scripts/nonEnglishMapper.py \
  -reducer scripts/nonEnglishReducer.py
  ```
  
### 3. View Results
- First 20 lines of word count:

`bash head -n 20 output/output_wordcount/part-00000`

- Total words in file1.txt:

`awk '{sum += $2} END {print sum}' output/output_wordcount/part-00000`

- First 20 lines of non-English words:

`head -n 20 output/output_nonenglish/part-00000`

- Total non-English words in file2.txt:

`awk '{sum += $2} END {print sum}' output output_nonenglish/part-00000`