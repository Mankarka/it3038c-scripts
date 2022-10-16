Matplotlib, is a helpful python package that is used to build plots, hence convert row data into visualized and easy to understand shapes.

### Installation ###

pip install -U matplotlib



^ Usage no.1 -- line plot
 
 np.arange(start,stop,step)
 these functions do what you expect,calculate  star, stop and steps count
 
 
 
^^ Usage no.2 -- Histograms

 The general format of Matplotlib's ax.hist()
 
 data and number bins could also be added to tht previuous fomart to look like:-
 
  ax.hist(data, num_bins)
  data is equivalent to the number of array of values to plot.
  
  bins are equivalent to the number of bars on the histogram
 
 
 
^^^ Usage no.3 -- 3D Surface Plots

ax.plot_surface(X, Y, Z)
while x and y only emphasise 2D surface the addition of the 'z' help give user the ability to 3D plot

rstride= and cstride=
determine the row step size and the column step size
