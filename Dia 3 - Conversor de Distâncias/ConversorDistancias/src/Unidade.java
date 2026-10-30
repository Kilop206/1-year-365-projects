public enum Unidade { 
    METRO("Metro"), 
    QUILOMETRO("Quilometro"), 
    MILHA("Milha"), 
    PE("Pé"); 

    private final String descricao; 

    Unidade(String descricao) { 
        this.descricao = descricao; 
    } 

    public String getDescricao() {
        return this.descricao;
    }
}
