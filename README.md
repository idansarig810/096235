# MMSE Test Application

**Note:** This application is in an early stage of development and some aspects are missing. Please refer to the following sections for details.

## Overview

The MMSE Test application is designed to assess cognitive function through a series of questions. It evaluates aspects such as space and time awareness, arithmetic abilities, speech, and memory.

## Missing Features

As this application is in its early stages, the following features are not yet implemented:

1. **Explanation at the End of the Test:** Currently, the test does not provide an explanation or summary of the results at the end.
2. **Saving Answers into a Database:** Responses are not saved into a database for analysis or tracking purposes.
3. **User Authentication:** The URL is generic for all users, and answers are shared among users who have access. Future development will include user-specific environments and prevent pre-saved answers from being accessible.

## Question Categories

- **Questions 1-5:** Space and Time Awareness
- **Questions 6-9:** Arithmetic Abilities
- **Questions 10-11:** Speech and Memory Assessment

## Algorithms Used

- **Questions 1-9:** Simple if-else algorithms are used for assessment.
- **Question 10:** Utilizes the Whisper "Tiny" model for speech assessment. The current model is efficient but less accurate. Future updates may include upgrading to a more accurate model.
- **Question 11:** Uses LlamaAPI for assessing sentences. The returned answers meet the criteria for the current stage of development, although improvements are planned for future versions.

## Getting Started

1. Clone the repository to your local machine.
2. Install the necessary dependencies.
3. Run the application.
