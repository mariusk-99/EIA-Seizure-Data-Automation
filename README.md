## Environmental Crime Database Automation Documentation

### Project Overview

The Environmental Investigation Agency (EIA) has spearheaded an innovative initiative to address the lack of a centralized repository for global environmental crime statistics. This gap in data has historically hindered the assessment of regulatory effectiveness in high-risk regions. Leveraging partnerships with various non-governmental organizations active in the environmental crime sector, the EIA has successfully established a comprehensive, open database. This repository, accessible [here](https://github.com/mariusk-99/EIA-Seizure-Data-Automation), has cataloged over 15,000 instances of environmental infractions worldwide since its inception.

### The Challenge

The manual data entry process previously in place was both labor-intensive and time-consuming, averaging 10-15 minutes per record. Relying heavily on volunteer contributions, the system faced significant scalability and data accuracy challenges. The inherent limitations of this approach capped the database's growth potential, with a yearly throughput of approximately 1,700 records. The need for an efficient, scalable, and accurate data processing method was clear.

### Innovation Through Automation

Recent advancements in Generative AI and Large Language Models (LLMs), particularly those developed by OpenAI, have shown remarkable potential for streamlining complex tasks. Recognizing this, the EIA embarked on research to explore the application of these technologies for automating the data entry process for its Environmental Crime database.

#### Implementation Framework

The automation process integrates several cutting-edge technologies and frameworks:

- **Web Scraping**: Utilizes the Python BeautifulSoup library to extract content from URLs listed in CSV files. The scraped content is then stored in a designated directory for further processing.

- **Data Extraction**: This stage involves sending the scraped content, along with specific instructions, to OpenAI's API. The returned data is structured in JSON format, with key-value pairs aligned with the database schema. For example:

```json
{
    "Country": "South Africa",
    "Town/Village": "Hoedspruit",
    "Date of incident": "27 May 2023",
    "Arrests made (Yes/No)": "Yes",
    "Number of arrests": 1,
    "Animal": "Rhino",
    "Incident Type": "Poaching",
    "Quantity": "Not specified",
    "Title": "Hoedspruit, Rhino Poaching Incident, 1 person arrested, 27 May 2023",
    "Vehicle type": "Car",
    "Transit method": "Road"
}
```

- **Data Loading**: An Azure AD application is configured to accept HTTP requests, facilitating the seamless integration of extracted records into the SharePoint database.

- **Manual Verification**: Despite the automation, a verification step remains crucial to ensure the integrity of the uploaded data. A detailed log of each upload's status aids in identifying and rectifying any discrepancies.

### Conclusion

The transition to an automated data processing system represents a significant leap forward in the EIA's ability to efficiently document environmental crimes on a global scale. This approach not only enhances the database's accuracy and scalability but also exemplifies the transformative potential of AI in environmental conservation efforts.
