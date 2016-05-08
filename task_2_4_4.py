with open("dataset_24465_4.txt", "r") as f1, open("f2.txt", "w") as f2:
    f2.write("\n".join(list(reversed([line.rstrip() for line in f1]))))