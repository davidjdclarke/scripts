import geopandas
import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
pandas_bokeh.output_notebook()

canada = geopandas.read_file("./gfsa000b11a_e.shp")
ontario = canada[canada['PRUID'] == '35']

# Sample data to plot
df=pd.DataFrame({'PCODE': ['P0V','P0L','P0T','P0Y', 'P0G', 'P2N'], 'A':[6,3,5,2,2,4] })

# Join ontario dataset with sample data
new_df=ontario.join(df.set_index('PCODE'), on='CFSAUID')


new_df.plot_bokeh(simplify_shapes=20000,
                  category="A",
                  colormap="Spectral",
                  hovertool_columns=["CFSAUID","A"])