from copy import deepcopy

def get_chart_layout(overrides: dict) -> dict:
  layout = dict(
      title="Placeholder",
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
          showgrid=False
      ),
      yaxis=dict(
          showgrid=True
      ),
      paper_bgcolor="white",
      plot_bgcolor="white",
  )

  layout.update(overrides)

  return deepcopy(layout)
