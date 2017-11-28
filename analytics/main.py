from analytics.operation_builder import build_operations_from_elem_ops
from analytics.parser import *
from analytics.visualization import *
import config

# path_to_csv = "..\\stian logs\\store.csv"
# list_of_elem_ops_per_pad = get_elem_ops_per_pad_from_ether_csv(path_to_csv)
path_to_db = "..\\etherpad\\var\\dirty.db"

config.path_to_db

list_of_elem_ops_per_pad = get_elem_ops_per_pad_from_db(path_to_db=path_to_db, editor='etherpad')
#list_of_elem_ops_per_pad = get_elem_ops_per_pad_from_db(editor='collab-react-components')

maximum_time_between_elem_ops = 7000  # milliseconds
pads = build_operations_from_elem_ops(list_of_elem_ops_per_pad,
                                                        maximum_time_between_elem_ops,
                                                        config.delay_sync,
                                                        config.time_to_reset_day,
                                                        config.time_to_reset_break,
                                                        config.length_edit,
                                                        config.length_delete)

for pad_name in pads:
    pad = pads[pad_name]
    print("PAD:", pad_name)
    print("TEXT:")
    print(pad.get_text())

    print('\nCOLORED TEXT BY AUTHOR')
    pad.display_text_colored_by_authors()

    print('\nCOLORED TEXT BY OPS')
    pad.display_text_colored_by_ops()

    print('\nSCORES')
    print('User proportion per paragraph score', pad.user_paticipation_paragraph_score())
    print('Proportion score:', pad.prop_score())
    print('Synchronous score:', pad.sync_score()[0])
    print('Alternating score:',pad.alternating_score())

    display_user_participation(pad)
    # plot the participation proportion per user per paragraphs
    display_user_participation_paragraphs(pad)
    display_user_participation_paragraphs_with_del(pad)

    # plot the proportion of synchronous writing per paragraphs
    display_proportion_sync_in_paragraphs(pad)

    # plot the overall type counts
    display_overall_op_type(pad)

    # plot the counts of type per users
    display_types_per_user(pad)

    # print('OPERATIONS')
    pad.display_operations()

    # print("PARAGRAPHS:")
    pad.display_paragraphs(verbose=1)
