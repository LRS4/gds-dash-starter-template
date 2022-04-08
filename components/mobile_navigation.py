from dash import dcc
from dash import html

mobile_navigation_bar = html.Div(
  children=[
    html.Ul(
        children=[
            html.Li(
                children=[
                    dcc.Link(
                        id="mobile-headlines-nav-button",
                        children="Headlines",
                        href="/section/home",
                        className="govuk-link govuk-link--no-visited-state"
                    ),
                    dcc.Link(
                        id="mobile-sales-nav-button",
                        children="Sales",
                        href="/section/avocado_sales",
                        className="govuk-link govuk-link--no-visited-state"
                    ),
                    dcc.Link(
                        id="mobile-map-nav-button",
                        children="Map",
                        href="/section/map",
                        className="govuk-link govuk-link--no-visited-state",
                    )
                ],
                className="moj-side-navigation__item"
            )
        ],
        className="govuk-list moj-side-navigation__list"
    )
  ],
  className="mobile-nav",
  id="mobile-navigation",
  style={"display": "none"}
)

htmlTemplate = dcc.Markdown('''
    <div class="mobile-nav" id="mobile-navigation" style="display: inline-block;">
        <ul class="govuk-list moj-side-navigation__list">
            <li class="moj-side-navigation__item moj-side-navigation__item--active">
                <a href="https://coronavirus.data.gov.uk/" aria-current="page" class="govuk-link govuk-link--no-visited-state">
                Daily update
                </a>
            </li>
            <li class="moj-side-navigation__item">
                <a href="https://coronavirus.data.gov.uk/details/testing" class="govuk-link govuk-link--no-visited-state">
                Testing
                </a>
            </li>
            <li class="moj-side-navigation__item"><a href="https://coronavirus.data.gov.uk/details/cases" class="govuk-link govuk-link--no-visited-state">Cases</a></li>
            <li class="moj-side-navigation__item"><a href="https://coronavirus.data.gov.uk/details/healthcare" class="govuk-link govuk-link--no-visited-state">Healthcare</a></li>
            <li class="moj-side-navigation__item"><a href="https://coronavirus.data.gov.uk/details/vaccinations" class="govuk-link govuk-link--no-visited-state">Vaccinations</a></li>
            <li class="moj-side-navigation__item"><a href="https://coronavirus.data.gov.uk/details/deaths" class="govuk-link govuk-link--no-visited-state">Deaths</a></li>
        </ul>
        <hr class="govuk-section-break govuk-section-break--m govuk-!-margin-top-3 govuk-!-margin-bottom-3 govuk-section-break--visible">
        <ul class="govuk-list moj-side-navigation__list">
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/details/interactive-map" class="govuk-link govuk-link--no-visited-state">Interactive maps</a></li>
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/metrics/category" class="govuk-link govuk-link--no-visited-state">Metrics documentation</a></li>
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/details/download" class="govuk-link govuk-link--no-visited-state">Download data</a></li>
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/details/whats-new" class="govuk-link govuk-link--no-visited-state">What's new</a></li>
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/details/developers-guide" class="govuk-link govuk-link--no-visited-state">Developer's guide</a></li>
            <li class="moj-side-navigation__item mobile"><a href="https://coronavirus.data.gov.uk/about" class="govuk-link govuk-link--no-visited-state">About</a></li>
        </ul>
        <hr class="govuk-section-break govuk-section-break--l govuk-!-margin-top-3 govuk-!-margin-bottom-3 govuk-section-break--visible">
    </div>
''', dangerously_allow_html=True)
