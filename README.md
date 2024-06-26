## Flask Application Design for Hindi Learning Website

### HTML Files

**- index.html (home page):**
- Contains the main interface with content on learning Hindi.
- Includes links to different sections of the website.

**- lessons.html (lessons page):**
- Displays a list of Hindi lessons, each with a title and description.
- Provides links to the corresponding lessons upon clicking.

**- lesson.html (individual lesson page):**
- Displays the content of a specific Hindi lesson.
- Includes text, images, and interactive exercises.

**- grammar.html (grammar page):**
- Provides a list of important Hindi grammar topics.
- Includes links to detailed explanations of each topic.

**- exercises.html (exercises page):**
- Contains interactive exercises to practice Hindi skills.
- Includes exercises for different levels of proficiency.

### Routes

**- / (home):**
- Displays the home page with a brief introduction and links to other sections.

**- /lessons:**
- Displays the lessons page with a list of available lessons.

**- /lesson/<lesson_id>:**
- Displays an individual lesson page for the specified lesson ID.

**- /grammar:**
- Displays the grammar page with a list of available grammar topics.

**- /grammar/<topic_id>:**
- Displays a detailed explanation of a specific grammar topic.

**- /exercises:**
- Displays the exercises page with a list of available exercises.

**- /exercise/<exercise_id>:**
- Displays an individual exercise for the specified exercise ID.

**- /submit-exercise:**
- Handles the submission of an exercise and returns feedback.

**- /progress:**
- Displays a user's progress in learning Hindi based on completed lessons and exercises.