# Load necessary libraries
library(tidyverse)

# Read the dataset
netflix <- read.csv("netflix_data.csv", stringsAsFactors = FALSE)

# Split the 'listed_in' column into individual genres
genres <- netflix %>%
  filter(!is.na(listed_in)) %>%
  separate_rows(listed_in, sep = ", ") %>%
  count(listed_in, sort = TRUE)

# Get the top 10 genres
top_genres <- genres %>% top_n(10, n)

# Plot the top 10 genres
ggplot(top_genres, aes(x = reorder(listed_in, n), y = n)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +
  labs(title = "Top 10 Most Common (Approx. Watched) Genres on Netflix",
       x = "Genre",
       y = "Number of Titles") +
  theme_minimal()
