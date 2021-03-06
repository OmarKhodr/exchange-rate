package exchange.api.models;
import com.google.gson.annotations.SerializedName;

public class User {
    @SerializedName("id")
    Integer id;

    @SerializedName("user_name")
    String username;

    @SerializedName("password")
    String password;

    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getUsername(){
        return username;
    }
}