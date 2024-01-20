from dash import  html, dcc, register_page

from utils.code_and_show import example_app, make_tabs
from utils.utils import app_description
from utils.other_components import  up_next, make_md
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: Theme Switch", path=links.theme_switch
)


text1 = """
# Dash AG Grid with light and dark themes

To learn all about AG Grid themes see Dash AG Grid docs [Layout and Styles](https://dash.plotly.com/dash-ag-grid/styling-themes) section.
 

## Bootstrap Light & Dark Color Modes

This site uses the Bootstrap Spacelab theme with a light and dark color mode switch.  You can see a complete tutorial on
 using [Bootstrap Color Modes](https://getbootstrap.com/docs/5.3/customize/color-modes/) at [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/adding-themes/color-modes).
 
Note that all the grids in this site automatically use the light or dark mode based on the app's theme. Try changing the theme with switch in the header.
 
This is achieved with a custom Alpine theme.  Learn more about [Customizing Themes] in the Dash docs, and at the Dash Bootstrap Theme Explorer [Dash AG Grid ](https://hellodash.pythonanywhere.com/adding-themes/ag-grid) section.
 

  
__Note: Requires Dash Bootstrap Components>=1.5.0__

"""

text2="""

## Change Grid Theme in a Callback

Another way to switch the theme is to update the `className` in a callback.  In this example, the grid is updated
 with either the `"ag-theme-quartz"` or `"ag-theme-quartz-dark"` theme based on the switch position by the grid.
 
  
"""

text3 = f"""

## AG Grid Auto dark themes

The 'auto' versions of each theme use the [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS media feature to switch between dark and light
 variants depending on whether the user has enabled dark mode on their operating system.
 
This is a cool feature, it would be great to have an `auto` mode for all Dash components!

Happy Coding!

"""



layout = html.Div(
    [
        make_md(text1),
        example_app("examples.get_started.V31_tutorial", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.styling.theme_switch_callback", make_layout=make_tabs),
        make_md(text3),
        up_next()
    ],
)
