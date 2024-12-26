library(ggplot2)
library(dplyr)
library(ggtext); library(svglite)
# Example for installing from a local file
install.packages("/path/to/AugSynth.tar.gz", repos = NULL, type = "source")
install.packages("devtools")

# Use devtools to install the package from GitHub
devtools::install_github("ebenmichael/augsynth")

library(augsynth)
?augsynth
?ggplot


#read data
df<-read.csv("/Users/shaokangyang/Library/CloudStorage/GoogleDrive-sky.ang510@gmail.com/My Drive/Nethealth/Data/CNSA/combine/7/df7_3hr.csv")
df <- df %>%
  filter(screen_time > 10)

# Assuming 'df' is the original dataframe
# Creating bins for screen time
bins <- seq(10, 185, by = 5)
df <- df %>%
  mutate(screen_time_bin = cut(screen_time, breaks = bins, right = FALSE, include.lowest = TRUE))

# Aggregating data
grouped <- df %>%
  group_by(screen_time_bin) %>%
  summarise(
    avg_sleep_debt = mean(sleep_debt, na.rm = TRUE),
    avg_message = mean(message, na.rm = TRUE),
    count = n()
  )

# Convert screen_time_bin to a factor for proper ordering
grouped <- grouped %>%
  mutate(screen_time_bin = factor(screen_time_bin, levels = unique(screen_time_bin)))

# Plotting
p <- ggplot(data = grouped, aes(x = screen_time_bin)) +
  # Line plot for sleep debt trend
  geom_line(aes(y = avg_sleep_debt, group = 1, color = "Sleep Debt"), size = 1) +
  geom_point(aes(y = avg_sleep_debt, color = "Sleep Debt"), size = 2) +
  geom_text(aes(y = avg_sleep_debt, label = round(avg_sleep_debt, 2)), 
            vjust = -0.5, color = "purple", size = 3) +
  # Line plot for message trend
  geom_line(aes(y = avg_message, group = 1, color = "Message"), linetype = "dashed", size = 1) +
  geom_point(aes(y = avg_message, color = "Message"), size = 2) +
  geom_text(aes(y = avg_message, label = round(avg_message, 2)), 
            vjust = -0.5, color = "darkorange", size = 3) +
  # Bar plot for number of observations
  geom_bar(aes(y = count, fill = "Number of Observations"), stat = "identity", alpha = 0.3, width = 0.4) +
  # Scales and axis labels
  scale_y_continuous(
    name = "Average Sleep Debt",
    sec.axis = sec_axis(~., name = "Message Count"),
    expand = expansion(mult = c(0, 0.1))
  ) +
  scale_color_manual(
    values = c("Sleep Debt" = "purple", "Message" = "darkorange"),
    guide = guide_legend(title = NULL)
  ) +
  scale_fill_manual(
    values = c("Number of Observations" = "lightgrey"),
    guide = guide_legend(title = NULL)
  ) +
  labs(
    x = "Screen Time (minutes)",
    title = "Trends of Sleep Debt, Messages, and Observations"
  ) +
  theme_minimal(base_family = "Times New Roman") +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, size = 12),
    axis.title.x = element_text(size = 14),
    axis.title.y = element_text(size = 14),
    legend.position = "top"
  )

# Save plot as SVG
ggsave("/Users/shaokangyang/Downloads/raw1.svg", p, width = 14, height = 8, dpi = 300, device = "svg")
