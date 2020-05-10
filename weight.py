# In[1]:


from loader import *


# In[ ]:


weights = utils.weights
weights_dict = utils.load_weights()

# Set layer weights of the model
for name in weights:
    if model.get_layer(name) != None:
        model.get_layer(name).set_weights(weights_dict[name])
