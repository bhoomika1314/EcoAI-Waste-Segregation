print("EcoAI - Smart Waste Segregation Assistant")

waste = input("Enter waste type (plastic, paper, glass, metal, organic): ").lower()

if waste == "plastic":
    print("Recycle in Plastic Bin")
elif waste == "paper":
    print("Recycle in Paper Bin")
elif waste == "glass":
    print("Recycle in Glass Bin")
elif waste == "metal":
    print("Recycle in Metal Bin")
elif waste == "organic":
    print("Dispose in Compost Bin")
else:
    print("Waste type not recognized")
