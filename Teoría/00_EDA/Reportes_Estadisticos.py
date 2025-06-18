from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="Profiling Report")

profile

import sweetviz as sv

my_report = sv.analyze(df)
my_report.show_html() # Nos tira error porque la version de pandas que
                      # utiliza es una mas antigua por lo que retrocedemos a la version "pip install numpy==1.23.4"

my_report.show_notebook()
