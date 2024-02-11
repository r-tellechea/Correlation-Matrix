import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.title('Correlation Matrix')

df = (
	pd.DataFrame({'A' : np.linspace(0,1,100)})
	.assign(B = lambda df : df.A + 1)
	.assign(C = lambda df : df.A * 2)
	.assign(D = lambda df : df.A * np.linspace(3,4,100))
	.assign(E = lambda df : np.log(df.A + 1))
	.assign(F = lambda df : np.cumsum(df.A))
	.assign(G = np.random.rand(100))
)

st.dataframe(df, use_container_width=True)

fig = px.imshow(
	(
		df
		.corr()
		.round(4)
	), 
	text_auto=True, 
	color_continuous_scale='RdYlGn',
	zmin=0,
	zmax=1,
)

fig.update_layout(
	xaxis={'side' : 'top', 'title_text' : 'Column X'},
	yaxis={'title_text' : 'Column Y'},
)
fig.update_coloraxes(showscale=False)

st.plotly_chart(fig, use_container_width=True)
