#!/usr/bin/env python
# coding: utf-8

# ## 1. Scala's real-world project repository data
# <p>With almost 30k commits and a history spanning over ten years, Scala is a mature programming language. It is a general-purpose programming language that has recently become another prominent language for data scientists.</p>
# <p>Scala is also an open source project. Open source projects have the advantage that their entire development histories -- who made changes, what was changed, code reviews, etc. -- are publicly available. </p>
# <p>We're going to read in, clean up, and visualize the real world project repository of Scala that spans data from a version control system (Git) as well as a project hosting site (GitHub). We will find out who has had the most influence on its development and who are the experts.</p>
# <p>The dataset we will use, which has been previously mined and extracted from GitHub, is comprised of three files:</p>
# <ol>
# <li><code>pulls_2011-2013.csv</code> contains the basic information about the pull requests, and spans from the end of 2011 up to (but not including) 2014.</li>
# <li><code>pulls_2014-2018.csv</code> contains identical information, and spans from 2014 up to 2018.</li>
# <li><code>pull_files.csv</code> contains the files that were modified by each pull request.</li>
# </ol>

# In[42]:


import pandas as pd

pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')
pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')
pull_files = pd.read_csv('datasets/pull_files.csv')


# In[43]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\n\ndef test_pulls_one():\n    correct_pulls_one = pd.read_csv(\'datasets/pulls_2011-2013.csv\')\n    assert correct_pulls_one.equals(pulls_one), \\\n    "Read in \'datasets/pulls_2011-2013.csv\' using read_csv()."\n\ndef test_pulls_two():\n    correct_pulls_two = pd.read_csv(\'datasets/pulls_2014-2018.csv\')\n    assert correct_pulls_two.equals(pulls_two), \\\n   "Read in \'datasets/pulls_2014-2018.csv\' using read_csv()."\n    \ndef test_pull_files():\n    correct_pull_files = pd.read_csv(\'datasets/pull_files.csv\')\n    assert correct_pull_files.equals(pull_files), \\\n    "Read in \'pull_files.csv\' using read_csv()."')


# ## 2. Preparing and cleaning the data
# <p>First, we will need to combine the data from the two separate pull DataFrames. </p>
# <p>Next, the raw data extracted from GitHub contains dates in the ISO8601 format. However, <code>pandas</code> imports them as regular strings. To make our analysis easier, we need to convert the strings into Python's <code>DateTime</code> objects. <code>DateTime</code> objects have the important property that they can be compared and sorted.</p>
# <p>The pull request times are all in UTC (also known as Coordinated Universal Time). The commit times, however, are in the local time of the author with time zone information (number of hours difference from UTC). To make comparisons easy, we should convert all times to UTC.</p>

# In[44]:


pulls = pulls_one.append(pulls_two, ignore_index=True)

pulls['date'] = pd.to_datetime(pulls['date'], utc= True)


# In[45]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_pulls_length():\n    assert len(pulls) == 6200, \\\n    'The DataFrame pulls does not have the correct number of rows. Did you correctly append pulls_one to pulls_two?'\n\ndef test_pulls_type():\n    assert type(pulls['date'].dtype) is pd.core.dtypes.dtypes.DatetimeTZDtype, \\\n    'The date for the pull requests is not the correct type.'")


# ## 3. Merging the DataFrames
# <p>The data extracted comes in two separate files. Merging the two DataFrames will make it easier for us to analyze the data in the future tasks.</p>

# In[46]:


data = pulls.merge(pull_files, on='pid')


# In[47]:


get_ipython().run_cell_magic('nose', '', '\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_merge():\n    assert len(data) == 85588, \\\n    \'The merged DataFrame does not have the correct number of rows.\'\n\ndef test_merge_dataframes():\n    correct_data = pulls.merge(pull_files, on=\'pid\')\n    also_correct_data = pull_files.merge(pulls, on=\'pid\')\n    assert correct_data.equals(data) or \\\n        also_correct_data.equals(data), \\\n        "The DataFrames are not merged correctly."        ')


# ## 4. Is the project still actively maintained?
# <p>The activity in an open source project is not very consistent. Some projects might be active for many years after the initial release, while others can slowly taper out into oblivion. Before committing to contributing to a project, it is important to understand the state of the project. Is development going steadily, or is there a drop? Has the project been abandoned altogether?</p>
# <p>The data used in this project was collected in January of 2018. We are interested in the evolution of the number of contributions up to that date.</p>
# <p>For Scala, we will do this by plotting a chart of the project's activity. We will calculate the number of pull requests submitted each (calendar) month during the project's lifetime. We will then plot these numbers to see the trend of contributions.</p>
# <ul>
# <li><p>A helpful reminder of how to access various components of a date can be found in <a href="https://campus.datacamp.com/courses/data-manipulation-with-pandas/slicing-and-indexing?ex=12">this exercise of Data Manipulation with pandas</a></p></li>
# <li><p>Additionally, recall that you can group by multiple variables by passing a list to <code>.groupby()</code>. This video from <a href="https://campus.datacamp.com/courses/data-manipulation-with-pandas/aggregating-dataframes?ex=9">Data Manipulation with pandas</a> should help!</p></li>
# </ul>

# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')

data['month'] = data['date'].dt.month

data['year'] = data['date'].dt.year

counts = data.groupby(['year','month'])['pid'].count()

counts.plot(kind='bar', figsize = (12,4))


# In[49]:


get_ipython().run_cell_magic('nose', '', '    \ndef test_group_and_count():\n    assert len(counts) == 74, \\\n    "The data was not grouped correctly. The history only spans 74 months."')


# ## 5. Is there camaraderie in the project?
# <p>The organizational structure varies from one project to another, and it can influence your success as a contributor. A project that has a very small community might not be the best one to start working on. The small community might indicate a high barrier of entry. This can be caused by several factors, including a community that is reluctant to accept pull requests from "outsiders," that the code base is hard to work with, etc. However, a large community can serve as an indicator that the project is regularly accepting pull requests from new contributors. Such a project would be a good place to start.</p>
# <p>In order to evaluate the dynamics of the community, we will plot a histogram of the number of pull requests submitted by each user. A distribution that shows that there are few people that only contribute a small number of pull requests can be used as in indicator that the project is not welcoming of new contributors. </p>

# In[50]:


get_ipython().run_line_magic('matplotlib', 'inline')

by_user = data.groupby('user').agg({'pid':'count'})

by_user.hist()


# In[51]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_by_user():\n    assert len(by_user) == 467 or len(by_user) == 464, \\\n    'The grouping by user is not correct'")


# ## 6. What files were changed in the last ten pull requests?
# <p>Choosing the right place to make a contribution is as important as choosing the project to contribute to. Some parts of the code might be stable, some might be dead. Contributing there might not have the most impact. Therefore it is important to understand the parts of the system that have been recently changed. This allows us to pinpoint the "hot" areas of the code where most of the activity is happening. Focusing on those parts might not the most effective use of our times.</p>

# In[52]:


last_10 = pulls.sort_values(by='date').tail(10)

joined_pr = pull_files.merge(last_10, on='pid')

files = set(joined_pr['file'])

print(files)


# In[53]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_last_10():\n    assert len(last_10) == 10, \\\n    'You need to select the last 10 pull requests.'\n\ndef test_join():\n    assert len(joined_pr) == 34, \\\n    'The join was not done correctly. You lost some pull requests in the process.'\n    \ndef test_no_files():\n    assert len(files) == 34, \\\n    'You did not select the right number of pull requests.'")


# ## 7. Who made the most pull requests to a given file?
# <p>When contributing to a project, we might need some guidance. We might find ourselves needing some information regarding the codebase. It is important direct any questions to the right person. Contributors to open source projects generally have other day jobs, so their time is limited. It is important to address our questions to the right people. One way to identify the right target for our inquiries is by using their contribution history.</p>
# <p>We identified <code>src/compiler/scala/reflect/reify/phases/Calculate.scala</code> as being recently changed. We are interested in the top 3 developers who changed that file. Those developers are the ones most likely to have the best understanding of the code.</p>

# In[54]:


file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

file_pr = data[data['file'] == file]

author_counts = file_pr.groupby('user').count()

author_counts.nlargest(3,'file')


# In[55]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_selecting_commits():\n    assert len(file_pr) == 30, \\\n    'You did not filter the data on the right file.'\n    \ndef test_author_counts():\n    assert len(author_counts) == 11, \\\n    'The number of authors is not correct.'")


# ## 8. Who made the last ten pull requests on a given file?
# <p>Open source projects suffer from fluctuating membership. This makes the problem of finding the right person more challenging: the person has to be knowledgeable <em>and</em> still be involved in the project. A person that contributed a lot in the past might no longer be available (or willing) to help. To get a better understanding, we need to investigate the more recent history of that particular part of the system. </p>
# <p>Like in the previous task, we will look at the history of  <code>src/compiler/scala/reflect/reify/phases/Calculate.scala</code>.</p>

# In[56]:


file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

file_pr = pull_files[pull_files['file'] == file]

joined_pr = pulls.merge(file_pr, on ='pid')

users_last_10 = set(joined_pr.nlargest(10,'date')['user'])

users_last_10


# In[57]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_join():\n    assert len(joined_pr) == len(file_pr), \\\n    'The join was not done correctly. You lost some pull requests in the process.'\n    \ndef test_file_pr():\n    assert len(joined_pr) == 30, \\\n    'The file does not have the correct number of pull requests.'\n    \ndef test_last_10():\n    assert len(users_last_10) == 6, \\\n    'You did not select the right number of pull requests.'")


# ## 9. The pull requests of two special developers
# <p>Now that we have identified two potential contacts in the projects, we need to find the person who was most involved in the project in recent times. That person is most likely to answer our questions. For each calendar year, we are interested in understanding the number of pull requests the authors submitted. This will give us a high-level image of their contribution trend to the project.</p>

# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')

authors = ['xeno-by', 'soc']

by_author = pulls[pulls['user'].isin(authors)]

counts = by_author.groupby([by_author['user'], by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()

counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)

counts_wide.plot(kind='bar')


# In[59]:


get_ipython().run_cell_magic('nose', '', '\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_author_pr():\n    assert len(by_author) == 715, \\\n    "The wrong number of pull requests have been selected."\n    \ndef test_counts():\n    assert len(counts) == 11, \\\n    \'The data should span 6 years.\'')


# ## 10. Visualizing the contributions of each developer
# <p>As mentioned before, it is important to make a distinction between the global expertise and contribution levels and the contribution levels at a more granular level (file, submodule, etc.) In our case, we want to see which of our two developers of interest have the most experience with the code in a given file. We will measure experience by the number of pull requests submitted that affect that file and how recent those pull requests were submitted.</p>

# In[60]:


authors = ['xeno-by', 'soc']
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

by_author = data[data['user'].isin(authors)]

by_file = by_author[by_author['file'] == file]

grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()

by_file_wide = grouped.pivot_table(index='date', columns='user', values='pid', fill_value=0)

by_file_wide.plot(kind='bar')


# In[61]:


get_ipython().run_cell_magic('nose', '', "\n# one or more tests of the students code. \n# The @solution should pass the tests.\n# The purpose of the tests is to try to catch common errors and to \n# give the student a hint on how to resolve these errors.\n\ndef test_by_author():\n    assert len(by_author) == 16999, \\\n    'Selecting by author did not produce the expected results.'\n    \ndef test_by_file():\n    assert len(by_file) == 15, \\\n    'Selecting by file did not produce the expected results.'\n    \n# def test_grouped():\n#     assert len(grouped) == 4, \\\n#     'There should be only 3 years that matches our data.'\n    \ndef test_by_file_wide():\n    assert len(by_file_wide) == 3, \\\n    'There should be only 3 years that matches our data.'")

