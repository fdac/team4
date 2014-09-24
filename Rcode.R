setwd("~/Documents/BusinessAnalytics/COSC 594/Project1/team4")
getwd()

library(ggplot2)
library(dplyr)

# Import data and some basic descriptives
d <- read.csv("reposNoNames.csv",
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

length(unique(d$owner)) # 188,874 unique user names 
  # supposedly more than 1 mil users total
  # about 80,000 "teams"
length(unique(d$language)) # 129 languages
length(unique(d$scm)) # 3 different scm values - there are dates
unique(d$scm)

library(ggplot2)
p.language <- ggplot( data = d, aes(x = language) )
p.language <- p.language + geom_histogram()
p.language
rm(p.language)



p.size <- ggplot ( data = d, aes(x = size) ) + geom_histogram()
p.size
rm(p.size)




# Ideas:
# tabulate number of repos using different scm technologies
# running calculation of repo creation rate and graph to show growth rate
# running sum of repos to show growth
# most popular language
# number of repos per technology


# technologies used
head(sort(unique(d$scm), decreasing = TRUE), 30)
  #html5 hg git then just numbers
length(d$scm[ which(d$scm == "hg") ])
length(d$scm[ which(d$scm == "git") ])
length(d$scm[!d$scm %in% c("hg", "git") ])


#### most popular languages
length(unique(d$language))
head(sort(table(d$language), decreasing = TRUE), 10)
head(sort(table(d$language), decreasing = TRUE), 10) / nrow(d)


#### repo size stats
summary(d$size)
mean(d$size)
qplot(log(size), data = d, geom = "histogram")
head(d$size[order(d$size, decreasing = TRUE)])

length(d$size[ which(d$size >= 1.25e8)])/nrow(d)

length(which(d$size == 0))
length(which(d$size < 1000))

#### repo lifetime stats
summary(d$activity)
qplot(activity, data = d, geom = "histogram")

# still active repos
length(which(Sys.Date() - d$updated_on < 30))
ggplot( data = d, aes(x = activity) ) + geom_histogram( binwidth = 50 )
 # most repositories are active for < 50 days - heavily skewed
qplot( activity, data = d[which(d$activity<51),], geom = "histogram")
 # looks like most repos are created and never updated or updated on the same day
length(which(d$activity == 0))
 # 175,308 repos




min(d$created_on, na.rm = TRUE)
max(d$created_on, na.rm = TRUE)
length(unique(d$created_on))

# trying to look at growth over time - create a running sum of repo
# count over the date range
library(dplyr)
date.groups <- group_by(d[order(d$created_on),], created_on)
head(date.groups)
date.count <- summarize(date.groups, repositories = n())
date.count$total <- cumsum(date.count$repositories)
date.count

qplot(x = created_on, y = total, data = date.count, geom = "line")
p <- ggplot(data = date.count, aes(x = created_on, y = total)) +
  geom_line() +
  xlab('Date') +
  ylab('Total Repositories') +
  ggtitle('Bitbucket Repository Growth')

## number of unique owners
length(unique(d$owner))

### active repos - updated at most 30 days ago
length(which(as.Date("2014-09-18", format = "%Y-%m-%d") - d$updated_on < 31))
length(which(as.Date("2014-09-18", format = "%Y-%m-%d") - d$updated_on < 31))/nrow(d)
