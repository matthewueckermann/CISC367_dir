# Impact of Industrial Activity on Community Health
*Matthew Ueckermann*

## Problem

I am interested in exploring how industrial pollution impacts the health of surrounding communities. Specifically, by following a 'thread' of my midterm assignment where I investigated toxic chemical releases, I am curious how these releases correlate with markers of community health. Two main correlations which come to mind are those between carcinogen releases, and cancer rates as well as the release of specific chemicals and asthma rates. I want to see if clear correlations exist between emissions and these health issues and if they do exist the magnitude of the effect.

## Background

Various industries release or cause the release of chemicals and particulates which have the potential to directly and severely impact the health and lives of those in the surrounding community. Releases of toxic chemicals are often mitigated to some extent to meet local air pollution licensing requirements and to prevent negative press attention. However, due to the nature of the equipment used as well as the effectiveness of mitigation technology, some releases will occur. While other industrial activities, like [mountain removal mining](https://en.wikipedia.org/wiki/Mountaintop_removal_mining#Health_impacts), necessitate the release of large amounts of particulates as well as toxic chemicals which cannot be easily controlled.

The fact that industries pollute chemicals which have been shown to be toxic in lab settings or which are believed to cause lung disorders, begs the question of whether these emissions have demonstrable effects on markers of community health. Do elevated quantities of exposure to these chemicals cause higher cancer rates? Or are chemicals emitted in small enough quantities that other factors dominate whether or not people develop certain disorders. This information equips communities with the knowledge about whether they should be concerned about surrounding industrial activity as well the extent to push for greater emission control or use of safer practices.

## Research Questions

- To what extent can the counties with higher than average rates of cancer be predicted by looking at carcinogen release from facilities in the same county?
- To what extent can counties with higher than average rates of asthma be predicted by looking at rates of nitrogen oxide and ozone releases?
- Do communities with a more active mining sector have a greater associated rate of asthma then those that do not?
- Do any routes of chemical release (air, water, landfill) cause a greater associated rate of cancer or asthma?

## Justification

For the first question, carcinogens are by [definition](https://www.cancer.gov/about-cancer/causes-prevention/risk/substances/carcinogens) those compounds which are believed to cause cancer. However, exposure limits have historically been defined in terms of [occupational exposure limits](https://www.cdc.gov/niosh/npg/nengapdxa.html), as these are where people are generally exposed to large enough quantities of these compounds frequently enough for them to make a difference. However, it is less straightforward to define exposure quantities which could cause surrounding communities to develop cancer at higher rates. Some studies show that atmospheric carcinogens in the UK have been linked with higher child cancer rates [1]. Completing a similar study in the US could give residents important knowledge about the facilities that surround them.

For the second question, it is widely accepted that exposure to particulates as well as oxides can trigger asthma attacks and may also lead to the development of new-onset asthma in some people [2]. It would be interesting to characterize whether emissions from industrial facilities play a role in exacerbating this condition, or if the particulates and other compounds which trigger asthma can be primarily attributed to transportation - another major source of these compounds. This could equip residents with extra knowledge of what to attribute their asthma too and what types of facilities to avoid to prevent triggering it.

The third question builds off of the second, by investigating the impact of mining specifically on asthma. This is because some forms of mining, namely mountain strip top, have been associated with increased amount of respiratory disorders, including asthma [3]. This builds on the history of lung disorders associated with mining, notably [black lung](https://en.wikipedia.org/wiki/Coalworker%27s_pneumoconiosis) in coal miners. This could show that entire communities, not just workers, are impacted by exposure brought about by the mining industry.

The fourth question is something that I am curious about. I would assume that for asthma to be caused by compounds that are emitted, it must be via the air. While for carcinogens, both air and water emissions would likely play a role. It would be interesting to see if changing the avenue of emissions could impact community health.


[1] Knox, E.G. (2005). Childhood cancers and atmospheric carcinogens. *Journal Epidemiol Community Healthy*, 59, 101-105. http://dx.doi.org/10.1136/jech.2004.021675
[2] Guarnieri, M. and Balmes, J.R. (2014). Outdoor air pollution and asthma. *Lancet*, 383(9928), 1561-1592. https://doi.org/10.1016/S0140-6736(14)60617-6
[3] Hendryx, M. (2013). Personal and family health in rural areas of Kentucky with and without mountaintop coal mining. *The Journal of Rural Health*, 29, s79-288. https://doi-org.udel.idm.oclc.org/10.1111/jrh.12016

## Datasets

To characterize chemical releases I plan to return to the dataset I used for the midterm, the  TRI which has data from 1987-2019 accessible in csv files [here](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-2019?). In this case; however, I will most likely only focus on the 2018 data, as for health indicators I plan to use the 2020 release of the "PLACES: Local Data from Better Health, Place Data 2020" which is released by the CDC [here](https://chronicdata.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx). 

The 2018 TRI data will be used as the PLACES dataset primarily pulls from survey data which was collected in 2018.

## Ethical Concerns and Considerations

Some ethical concerns:

- Failing to find a correlation between chemical releases and health concerns does not mean that they do not exist. Some stakeholders like chemical or mining companies could use this as evidence that their facilities do not impact the surrounding community when it really does. Residents with their health adversely effected, another stakeholder, may then have a harder time advocating for greater control of releases or winning much needed settlements from these companies. 
- Similar to above, finding a correlation between these chemical releases and health concerns also does not mean that they are real, as I am not controlling for covariates. Because of this the major stakeholders mentioned above cannot jump to any conclusions, specifically the residents stating that the surrounding industry is responsible for specific pollution. Instead, they should use this analysis as an impetus to complete more research in their specific community.
- Other stakeholders involved are local hospitals and healthcare providers who may want knowledge how the industry around them impacts their patients. They may take into consideration the types of chemicals emitted by the industry in the surrounding area in the way they diagnose or certain disorders. As they might expect that a disorder might be one that has been connected to a chemical that is emitted in the community and might treat as such, even if that is not the case. Because of this, we will have to clarify that these are community results that should not be taken for diagnosis purposes.  

Some data analysis considerations:
- Covariates generally need to be controlled for in this type of analysis; however, this is not possible with the datasets available.
- County wide data might dilute the impact of local facilities on community health. 
    - Similarly, the PLACES dataset does warn against excessive extrapolation of the county results due to low sample sizes; therefore, results must be taken with some skepticism and should provide an impetus for further study.
