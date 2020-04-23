from PW_explorer.load_worlds import load_worlds
from PW_explorer.run_clingo import run_clingo
import networkx as nx

class WODBVizLib:

    GRAPHVIZ_PROPERTY_REDIRECTION_DICT = {
        'color': 'fillcolor',
        'size': ['height', 'width'],
    }

    GRAPHVIZ_PROPERTY_VALUE_REDIRECTION_DICT = {
        'shape': {
            'square': 'box',
        },
        'height': {
            'large': 2.5,
            'small': 1,
        },
        'width': {
            'large': 2.5,
            'small': 1,
        },
        'style': {
            'bold': '"filled,bold"',
            'thin': 'filled'
        }
    }

    @staticmethod
    def create_figure(df, property_name_column='property_name',
                      property_value_column='property_value',
                      figID_column='figure_ID', figID=None):

        # If multiple figures are in the dataframe, then clip to retain only the required figure
        if figID is not None:
            df = df[df[figID_column] == figID]
        else:
            if len(df) <= 0:
                return None
            figID = df.iloc[0][figID_column]

        G = nx.Graph()
        G.add_node(figID)

        for i, row in df.iterrows():
            prop_name = row[property_name_column]
            prop_value = row[property_value_column]

            if prop_name in WODBVizLib.GRAPHVIZ_PROPERTY_REDIRECTION_DICT:
                prop_name = WODBVizLib.GRAPHVIZ_PROPERTY_REDIRECTION_DICT[prop_name]

            if not isinstance(prop_name, list):
                prop_name = [prop_name]

            for p in prop_name:
                if (p in WODBVizLib.GRAPHVIZ_PROPERTY_VALUE_REDIRECTION_DICT) \
                and (prop_value in WODBVizLib.GRAPHVIZ_PROPERTY_VALUE_REDIRECTION_DICT[p]):
                    prop_value = WODBVizLib.GRAPHVIZ_PROPERTY_VALUE_REDIRECTION_DICT[p][prop_value]

                G.nodes[figID][p] = prop_value
        return G

    @staticmethod
    def visualize_figures(propDB_df, property_name_column='property_name',
                      property_value_column='property_value',
                      figID_column='figure_ID', figIDs_to_visualize=None, graph_label=" "):

        if figIDs_to_visualize is not None:
            propDB_df = propDB_df[propDB_df[figID_column].isin(figIDs_to_visualize)]

        propDB_grouped_by_figID = propDB_df.groupby(figID_column)
        figureIDs = list(propDB_grouped_by_figID.groups.keys())

        gs = {}
        for figID in figureIDs:
            g = WODBVizLib.create_figure(propDB_grouped_by_figID.get_group(figID), figID=figID,
                                         property_name_column=property_name_column,
                                         property_value_column=property_value_column,
                                         figID_column=figID_column)
            gs[figID] = g

        G = nx.union_all(gs.values())
        G.graph['label'] = graph_label

        return G

    @staticmethod
    def visualize_wodb_query_instance(propDB_df, soln_df,
                                      property_name_column='property_name',
                                      property_value_column='property_value',
                                      figID_column='figure_ID', soln_figID_colum='x1',
                                      graph_label=" "):

        G = WODBVizLib.visualize_figures(propDB_df, property_name_column='property_name',
                                         property_value_column='property_value',
                                         figID_column='figure_ID', graph_label=graph_label)

        figIDs_soln = [row[soln_figID_colum] for i, row in soln_df.iterrows()]

        for figID in figIDs_soln:
            G.nodes[figID]['label'] = "{}\n(TODB)".format(figID)
        G.graph['forcelabels'] = True

        return G

    @staticmethod
    def visualize_figure_from_asp_rules(db_asp_rules, db_rel_name='propDB', db_rel_arity=3,
                                    property_name_column='property_name',
                                    property_value_column='property_value',
                                    figID_column='figure_ID', figIDs_to_visualize=None):

        asp_output, md = run_clingo(db_asp_rules)
        pws_rels_dfs, rel_schemas, pw_objects = load_worlds(asp_output, meta_data=md, silent=True)
        propDB_df_rel_name = "{}_{}".format(db_rel_name, str(db_rel_arity))
        propDB_df = pws_rels_dfs[propDB_df_rel_name]
        # Assumes that running the reasoner will only produce one PW (or that atleast all of them have the same DB)
        propDB_df = propDB_df[propDB_df['pw'] == 1]

        return WODBVizLib.visualize_figures(propDB_df, property_name_column=property_name_column,
                                            property_value_column=property_value_column,
                                            figID_column=figID_column,
                                            figIDs_to_visualize=figIDs_to_visualize)