def height_notation(plot_name , coordinator , dataframe , color="white", percent = False):
    total = len(dataframe)
    for p in plot_name.patches:
        height = p.get_height().round(2)
        text = str(float(height))
        if percent == True:
            plot_name.text(p.get_x() + p.get_width() / 2 , height + coordinator , text + ' | ' + str(height * 100 // total) + '%' , ha = 'center', color="white")
        else:
            plot_name.text(p.get_x() + p.get_width() / 2 , height + coordinator , text , ha = 'center', color=color)