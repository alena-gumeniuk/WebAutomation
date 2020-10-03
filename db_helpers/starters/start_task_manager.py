import json

from db_helpers.task_manager import TaskManager

task_manager = TaskManager()
# records = task_manager.get_all_tasks('miner')
# records = task_manager.get_task_for_execution('miner')

# task_manager.insert_into_tasks(skill='watch', arguments=json.dumps(['date', 'Kazakhstan. Premier League',
#                                                                     'Orda\'basy', 'Taraz'],
#                                                                    ensure_ascii=False),
#                                attempts=0, worker_type='better',
#                                state='waiting for execution')


game = json.dumps([{'Date of Match': '27.09', 'Time of Match': '12:30',
                    'Tournament name': 'some tournament', 'Left command name': 'left',
                    'Right command name': 'right'}])
task_manager.add_games({'result': game})

# task_manager.change_task_state('completed', 1)
# print(json.loads(records))
