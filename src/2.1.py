import pandas as pd
import sys
import matplotlib.pyplot as plt
import warnings

if __name__ == '__main__':
    penguins = pd.read_csv(sys.argv[1])

    print("###### Atribut exploration\n")

    print("#### Kategorické\n")
    include = ['object']
    print(penguins.describe(include = include))
    print("")


    print("## Species\n--------")
    print(penguins.species.value_counts())
    print(penguins.species.value_counts(normalize=True).mul(100).round(1).astype(str)+'%')
    print("")

    print("## Island\n--------")
    print(penguins.island.value_counts())
    print(penguins.island.value_counts(normalize=True).mul(100).round(1).astype(str)+'%')
    print("")

    print("## Sex\n--------")
    print(penguins.sex.value_counts())
    print(penguins.sex.value_counts(normalize=True).mul(100).round(1).astype(str)+'%')
    print("")


    print("#### Číselné\n")
    print(penguins.describe())
    print("")

    print("###### Missing values\n")
    print(penguins.isnull().sum())
    print("")
    sum = 0
    moreThanTwo = 0
    for i in penguins.index:
        amount = penguins.loc[i].isnull().sum()
        if amount > 0:
            sum = sum + 1
            print(f'Record with missing value {sum} on row {i}')
            print(penguins.loc[i])
            print("")
            if amount > 1:
                moreThanTwo = moreThanTwo + 1
    print(f'Total rows with missing value: {sum}')
    print(f'Total rows with more than two missing value: {moreThanTwo}')
    print("")

    ###### GRAPHS ########
    warnings.filterwarnings(action='ignore', category=UserWarning)

    male = penguins.loc[ penguins['sex']=='MALE'].dropna()
    female = penguins.loc[ penguins['sex']=='FEMALE'].dropna()

    adelie = penguins.loc[ penguins['species']=='Adelie'].dropna()
    chinstrap = penguins.loc[ penguins['species']=='Chinstrap'].dropna()
    gentoo = penguins.loc[ penguins['species']=='Gentoo'].dropna()
    speciesColors = ['#eeee00', '#00ee00', '#00eeee']

    dataSpeciesLength = [adelie['culmen_length_mm'], chinstrap['culmen_length_mm'], gentoo['culmen_length_mm']]
    dataSpeciesDepth = [adelie['culmen_depth_mm'], chinstrap['culmen_depth_mm'], gentoo['culmen_depth_mm']]
    dataSpeciesFlipper = [adelie['flipper_length_mm'], chinstrap['flipper_length_mm'], gentoo['flipper_length_mm']]
    dataSpeciesMass = [adelie['body_mass_g'], chinstrap['body_mass_g'], gentoo['body_mass_g']]

    columnName = ['culmen length (mm)', 'culmen depth (mm)', 'flipper length (mm)', 'body mass (g)']
    rowName = ['sex', 'species']
    speciesName = ['Adelie', 'Chinstrap', 'Gentoo']

    fig, axs = plt.subplots(2,4)

    for ax, col in zip(axs[0], columnName):
        ax.set_title(col)
    
    for ax, row in zip(axs[:,0], rowName):
        ax.set_ylabel(row, rotation=90, size='large')

    fillA = [' ' for item in male['culmen_length_mm']]
    fillA = ['  ' for item in male['culmen_length_mm']]
    xMale = ['Male' for item in male['culmen_length_mm']]
    xFemale = ['Female' for item in female['culmen_length_mm']]
    axs[0,0].scatter(xFemale,female['culmen_length_mm'])
    axs[0,0].scatter(xMale,male['culmen_length_mm'])

    axs[0,1].scatter(xFemale,female['culmen_depth_mm'])
    axs[0,1].scatter(xMale,male['culmen_depth_mm'])

    axs[0,2].scatter(xFemale,female['flipper_length_mm'])
    axs[0,2].scatter(xMale,male['flipper_length_mm'])

    axs[0,3].scatter(xFemale,female['body_mass_g'])
    axs[0,3].scatter(xMale,male['body_mass_g'])


    axs[1,0].set_xticklabels(speciesName)
    box = axs[1,0].boxplot(dataSpeciesLength, patch_artist=True)
    for patch, color in zip(box['boxes'], speciesColors):
        patch.set_facecolor(color)

    axs[1,1].set_xticklabels(speciesName)
    box = axs[1,1].boxplot(dataSpeciesDepth, patch_artist=True)
    for patch, color in zip(box['boxes'], speciesColors):
        patch.set_facecolor(color)

    axs[1,2].set_xticklabels(speciesName)
    box = axs[1,2].boxplot(dataSpeciesFlipper, patch_artist=True)
    for patch, color in zip(box['boxes'], speciesColors):
        patch.set_facecolor(color)

    axs[1,3].set_xticklabels(speciesName)
    box = axs[1,3].boxplot(dataSpeciesMass, patch_artist=True)
    for patch, color in zip(box['boxes'], speciesColors):
        patch.set_facecolor(color)

    plt.show()

    print("### TESTING")
