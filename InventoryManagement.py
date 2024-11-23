class InventoryManager:
    def __init__(self):
        self.sections = {}
    
    def add_section(self, section):
        self.sections[section.name] = section

    def get_section(self, name):
        return self.sections.get(name)
    
    def add_item(self, section_name, item):
        section = self.get_section(section_name)
        if section:
            section.add_item(item)
        else:
            raise ValueError("Section not found!")
    
    def get_items_in_section(self, section_name):
        section = self.get_section(section_name)
        if section:
            return [str(item) for item in section.items.values()]
        return []

    # Creating function that gets all items, no matter the section
    def get_all_items(self):
        all_items = []
        # Go through both sections aka 'Electronics' and 'Automotive'
        for section in self.sections.values():
            # Gets items in each section
            for item in section.items.keys():
                # Adds it to all_items list
                all_items.append(item)
        return all_items

    def add_stock(self, section_name, name, amount, misc_info = "a"):
        section = self.get_section(section_name)
        if section:
            section.add_stock(name, amount, misc_info)
        else:
            raise ValueError("Section not found!")
        
    def remove_stock(self, section_name, name, amount):
        section = self.get_section(section_name)
        if section:
            try:
                section.remove_stock(name, amount)
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Section not found!")
        
    def move_stock(self, from_section_name, to_section_name, item_name, amount):
        from_section = self.get_section(from_section_name)
        to_section = self.get_section(to_section_name)

        if from_section and to_section:
            try:
                from_section.remove_stock(item_name, amount)
                to_section.add_stock(item_name, amount,"m")
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Value(s) not found!")
        
    def get_inventory(self):
        inventory = []
        for section in self.sections.values():
            inventory.append(str(section))
            inventory.extend(str(item) for item in section.items.values())
        return inventory

    # Function to get stock items that are below a certain threshold
    def get_low_stock_items(self):
        # List to store items
        low_stock_items = []
        # Gets the items that have a quantity level of 1 or below
        for section in self.sections.values():
            for item in section.items.values():
                if item.quantity <= 1:
                    low_stock_items.append(item.name)
        # Returns list so it can be used in main.py
        return low_stock_items
