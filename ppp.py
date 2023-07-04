
Pipeline(

  nodes = [

  {"name": "par_1", "source": ("user_input", "user_input_1"), "service": Paraphrase},

  {"name": "par_2", "source": ("user_input", "user_input_2"), "service": Paraphrase},

  {"name": "par_3", "source": ("user_input", "user_input_3"), "service": Paraphrase},

  {"name": "search_1", "source": ("par_1", "paraphrase")},

  {"name": "search_2", "source": ("par_2", "paraphrase")},

  {"name": "search_3", "source": ("par_3", "paraphrase")},

]

