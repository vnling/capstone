# aer: 84-113
# eco: 69-91
# jpe: 125-131
# qje: 109-138
# res: 61-90

START=61
END=90
JOURNAL="res"
for ((i=START;i<=END;i++)); do
    python3 code/aggregate_names.py extracted_names/${JOURNAL}/${JOURNAL}.${i}.extracted.txt extracted_names/${JOURNAL}.aggregate.txt
done