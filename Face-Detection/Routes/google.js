const express=require("express");
const router=express.Router();
const passport=require("passport");
const {ensureAuthenticated}=require("../Config/auth");



router.get("/",passport.authenticate('google',{scope:['profile','email']}));

router.get("/callback",passport.authenticate("google",{failureRedirect:"/"}),(req,res)=>{
    res.redirect("/");
})

module.exports=router;
