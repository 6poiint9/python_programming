#!/usr/bin/env python
# coding: utf-8

# <img src="images/00-mathematics_with_python.png" style="height:250px" align="left">

# <!--NAVIGATION-->
# | [I Introduction to Python](10-introduction_to_python.ipynb) |  [2 Basic Data Types](12-basic_data_types.ipynb) >

# # 1 Python Basics
# ## 1.1 Python as a calculator
# Jupyter notebooks offer different types of cells.
# Markdown cells are used for text.
# In a code cell program statements may be executed.
# Similar to a calculator, the result of the calculation is displayed immediately.

# In[19]:


(3+2 * 6) / 6 - 3 


# If the result of a calculation is assigned to a variable, no output appears.

# In[20]:


x=3+2


# The value of a variable can be output using the [print()](https://docs.python.org/3/library/functions.html#print) function.

# In[21]:


print(x)


# Variables can be used in other code cells.

# In[22]:


x+4


# ## 1.2 Mathematical operators
# There are five elementary mathematical operators in Python.
# Each operator can be combined with the equal sign.
# 
# $
# \begin{array}{|l|l|l|l|l|}
# \hline
# \mbox{addition} & \mbox{subtraction} & \mbox{multiplication} & \mbox{division} & \mbox{power} \\
# \hline
# + & - & * & / & ** \\
# \hline
# += & -= & *= & /= & **= \\
# \hline
# \end{array}
# $

# In[23]:


x*=2
print(x)


# 
# 
# 

# In[ ]:




