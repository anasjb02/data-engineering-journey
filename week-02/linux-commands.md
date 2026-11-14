cd ~/de-bootcamp/ostad-de-bootcamp-main

echo "Assignment 2 — Anas" > assignment-02.txt
echo "" >> assignment-02.txt
echo "1. CSV line: $(wc -l < module-01/data/orders_oct2026.csv) (46,907 orders + 1 header)" >> assignment-02.txt
echo "2. log line: $(wc -l < module-01/data/app_2026-10.log)" >> assignment-02.txt
echo "3. WARN: $(grep -c "| WARN" module-01/data/app_2026-10.log)" >> assignment-02.txt
echo "4. DEBUG: $(grep -c "| DEBUG" module-01/data/app_2026-10.log)" >> assignment-02.txt
echo "5. 10 Oct ERROR: $(grep "^2026-10-10" module-01/data/app_2026-10.log | grep -c "| ERROR |")" >> assignment-02.txt
echo "6. Most WARN: $(grep "| WARN" module-01/data/app_2026-10.log | cut -c1-10 | sort | uniq -c | sort -rn | head -1)" >> assignment-02.txt
echo "7. bKash orders: $(grep -c "bKash" module-01/data/orders_oct2026.csv)" >> assignment-02.txt
echo "" >> assignment-02.txt
echo "Bonus" >> assignment-02.txt
echo "8. auth ERROR: $(grep "| ERROR |" module-01/data/app_2026-10.log | grep -c "auth")" >> assignment-02.txt
echo "9. Lowest ERROR: $(grep "| ERROR |" module-01/data/app_2026-10.log | cut -c1-10 | sort | uniq -c | sort -n | head -1)" >> assignment-02.txt

cat assignment-02.txt
