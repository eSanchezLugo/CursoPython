class Club:
    def __init__(self, nombre):
        self.nombre = nombre,
        self.jugadores = []
        
    def __len__(self):
        return len(self.jugadores)
    
    def __getitem__(self, i):
        return self.jugadores[i]
    
    
    def __repr__(self):
        return f"Club {self.nombre}: {self.jugadores}"
    
    
    def __str__(self):
        return f"Club {self.nombre} con {len(self)} jugadores"
        
        

