# Midterm Project Background
*Matthew Ueckermann*

## Problem to explore: Chemical Releases

I am planning on exploring the [Toxics Release Inventory (TRI)](https://en.wikipedia.org/wiki/Toxics_Release_Inventory) which is a dataset containing all chemicals released by manufacturing plants in the U.S. which are reported to the EPA. This was established in 1986 to bring transparency to the chemical industry, partially as a reaction to the [1984 Bhopal disaster](https://en.wikipedia.org/wiki/Bhopal_disaster). This dataset was introduced to me in one of my previous courses (CHEG613: Energy and the Environment) as one of the most efficient pieces of environmental legislation; however, I have not had the opportunity to explore it.

In chemical manufacturing it is impossible not to release some amount of toxic chemicals (pressure equipment, incinerators, and wastewater treatment can never be perfect) while accidents will also cause unintended releases. The report is useful as it breaks down the location of the releases (onsite water discharge, offsite water treatment, landfill, release to air, and much more). It also allows one to search chemical released based on general toxicity as it notes persistent and bioaccumulate compounds (PBTs) as well as dioxins, both of which are particularly nasty. 

Helpful resource https://www.epa.gov/toxics-release-inventory-tri-program/timeline-toxics-release-inventory-milestones

## Problem to explore

How do releases in the TRI correlate with year, state, and county location? Specifically:
- Do chemical plants get better at controlling emissions over time?
- Does the composition of chemicals released by a facility change over time? Or in other words will a facility get better at controlling the emissions of one chemical versus another?
- Have plants shifted from releasing PBTs and dioxins over time?
- Is there any "red state"-"blue state" effect?
- Can you see the impact of environmental regulation, or the loosening of it by administration?


## Justification

Chemical releases, especially of toxic chemicals, are important to manage and minimize. Knowledge of how chemical plants minimize releases from year to year, as well as if there is any geographic variation could be important in accessing environmental regulations and industrial best practices. Similarly, looking at overall trends is important to ensure that the industry is getting cleaner, trending in a more sustainable direction.

As far as evidence, I think it is safe to say that toxic chemical emissions and their prevention is an important problem. One way to demonstrate this is by looking at the EPA, who constantly try to reduce these emission through programs like the [clean air act in 1970](https://www.epa.gov/clean-air-act-overview/progress-cleaning-air-and-improving-peoples-health). While this specific research using the TRI can be motivated by interesting research that has already done using the dataset, including looking at correlations between chemical releases and community composition [1]. The impact of involving employees in pollution abatement programs on emissions [2]. As well as the overall impact that the TRI had on changes in stock prices after the first reporting of it [3]. However, all of these studies are relatively old (published sometime in the 90s), meaning that they miss out on two decades worth of trends, motivating a new look at the TRI.

Works Cited
1. Arora, S., Cason, T. N., Arora, S. & Casont, T. N. Do Community Characteristics Influence Environmental Outcomes? Evidence from the Toxics Release Inventory Southern Economic Association, 65, 691–716 (1999).
2. Bunge, J., Cohen-rosenthal, E. & Ruiz-quintanilla, Employee participation in pollution reduction : preliminary analysis of the Toxics , Release Inventory. Journal of cleaner Production 4, 9–16 (1996).
3. Konar, S., Cohen, M. Information As Regulation : The Effect of Community Right to Know Laws on Toxic Emissions. Journal of Environmental Economics and Management, 32, 109–124 (1997).


## Data set to be used

As stated I am going to use the TRI which has data from 1987-2019 accessible in csv files [here](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-2019?).

Documentation about the dataset is given in this [pdf](https://www.epa.gov/sites/production/files/2019-08/documents/basic_data_files_documentation_aug_2019_v2.pdf).

## Ethical concerns and other considerations

Some ethical concerns and  I have about my analysis include:
- As a chemical engineering major entering industry (although in a more sustainable chem company) I will have my own biases about the industry and will probably not be as critical as someone who is not.
- Chemical companies could use this analysis as evidence that they do better than their peers or other in a geographic area, which may disincentivize improvement.
- I am not an expert of the toxicity of different chemicals, I know generally PBTs/dioxins are worse than others on the list but there is not necessarly a consensus on all chemicals on the list. Treating them the same would be disingenuous, but may be necessary for this level.
- Mentioning a "red state" - "blue state" effect implicitly assumes that the "red states" will allow for more emissions than blue states.



Other considerations/compounding factors:
- The geographical distribution of chemical plants is skewed, i.e. there are a lot of petroleum refineries in Texas, but none in Massachusetts.
- You reach a level in emissions control technology where it can be hard (and costly) to improve, expecting plants to improve year to year is not realistic.
- Controlling by facility size is required in looking at fugitive air emissions as they are a function of the amount of pressurized equipment.
- Changing the composition of chemicals released may be more indicative of a change in product, not of a change in the process.
