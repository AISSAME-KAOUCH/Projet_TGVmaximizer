from view.start_view import StartView

if __name__ == '__main__':
    # run the StartView
    current_view = StartView()

    while current_view:
        
        print('-----------------')
        current_view.display_info()
        current_view = current_view.make_choice()
