setwd("~/Documents/BusinessAnalytics/COSC 594/Project1/team4")
getwd()

# Import data and some basic descriptives
d <- read.csv("allPublicRepos.csv",
              fileEncoding="UTF-8",
              quote = "",
              stringsAsFactors = FALSE,
              strip.white = TRUE)
dim(d)
names(d)
str(d)
head(d)

# Convert date fields to date types (imported as character)
d$created_on <- as.Date(d$created_on, format = "%Y-%m-%d")
head(d$created_on)
mode(d$created_on)
class(d$created_on)
d$updated_on <- as.Date(d$updated_on, format = "%Y-%m-%d")
head(d$updated_on)
mode(d$updated_on)
class(d$updated_on)

d$activity <- as.numeric( d$updated_on - d$created_on )
head(d$activity)

length(unique(d$owner)) # 189,047 unique user names 
  # supposedly more than 1 mil users total
  # about 80,000 "teams"
length(unique(d$language)) # 322 languages
length(unique(d$scm)) # 240 different scm values


library(ggplot2)
p.language <- ggplot( data = d, aes(x = language) )
p.language <- p.language + geom_histogram()
p.language
rm(p.language)

p.activity <- ggplot( data = d, aes(x = activity) ) + geom_histogram( binwidth = 50 )
p.activity # most repositories are active for < 50 days - heavily skewed
rm(p.activity)

p.size <- ggplot ( data = d, aes(x = size) ) + geom_histogram()
p.size
rm(p.size)



# Ideas:
# tabulate number of repos using different scm technologies
# running calculation of repo creation rate and graph to show growth rate
# running sum of repos to show growth
# most popular language
# number of repos per technology


