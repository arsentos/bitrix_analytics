files = ["./numbers.txt", "./a_e.txt", "./f_j.txt", "./k_o.txt", "./p_t.txt", "./u_z.txt"]
total = 0
# with open("./yapl_ru_sites.txt", "r") as yapl:
#     for line in yapl.readlines():
#         total += 1
#     print(total)
with open("./yapl_ru_sites.txt", "w") as yapl:
    for file in files:
        with open(file, "r",) as f:
            for line in f.readlines():
                yapl.write(f"{line}")
                total +=1
print(total)