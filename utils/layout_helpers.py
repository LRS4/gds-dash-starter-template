from copy import deepcopy

def get_chart_layout(title: str):
  layout = dict(
      title=title,
      titlefont=dict(
          family="GDS Transport",
          size=19
      ),
      hoverlabel=dict(
          font=dict(
            family="GDS Transport",
            size=16
          )
      ),
      xaxis=dict(
          showgrid=False,
          fixedrange=True
      ),
      yaxis=dict(
          showgrid=True,
          fixedrange=True,
          tickprefix="$"
      )
  )

  return deepcopy(layout)
