import React, { useState, useEffect } from "react";
// bootstrap
import Col from "react-bootstrap/Col";	
import Row from "react-bootstrap/Row";	
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
// css
import appStyles from "../../App.module.css";
import styles from "../../styles/PostsPage.module.css";
// component
import Post from "./Post";
import Asset from "../../components/Asset";
import { useLocation } from "react-router";
import { axiosReq } from "../../api/axiosDefaults";
import InfiniteScroll from "react-infinite-scroll-component";
import { fetchMoreData } from "../../utils/utils";
import PopularProfiles from "../profiles/PopularProfiles";
import { useCurrentUser } from "../../contexts/CurrentUserContext";

function PostsPage({message}) {

    const [posts, setPosts] = useState({ results: [] });
    const [hasLoaded, setHasLoaded] = useState(false);
    const { pathname } = useLocation();
    const [query, setQuery] = useState("");
    const currentUser = useCurrentUser();

    useEffect(() => {
        const fetchPosts = async () => {
          try {
            const { data } = await axiosReq.get(`/posts/?search=${query}`);
            setPosts(data);
            setHasLoaded(true);
          } catch (err) {
            // console.log(err);
          }
        };
    
        setHasLoaded(false);
        const timer = setTimeout(() => {
          fetchPosts();
        }, 1000);
    
        return () => {
          clearTimeout(timer);
        };
      }, [query, pathname, currentUser]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2 " lg={8}>
        <PopularProfiles mobile/>
        <i className={`fas fa-search ${styles.SearchIcon}`} />
        <Form
          className={styles.SearchBar}
          onSubmit={(event) => event.preventDefault()}
        >
          <Form.Control
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            type="text"
            className="mr-sm-2"
            placeholder="Search Posts"
          />
        </Form>
        {hasLoaded ? (
          <>
            {posts.results.length ? (
              <InfiniteScroll
                children={posts.results.map((post) => (
                  <Post key={post.id} {...post} setPosts={setPosts} />
                ))}
                dataLength={posts.results.length}
                loader={<Asset spinner />}
                hasMore={!!posts.next}
                next={() => fetchMoreData(posts, setPosts)}
              />
            ) : (
              <Container className={appStyles.Content}>
                <Asset
                 icon="fa-brands fa-searchengin"
                 message={message} />
              </Container>
            )}
          </>
        ) : (
          <Container className={appStyles.Content}>
            <Asset spinner />
          </Container>
        )}
      </Col>
      <Col md={4} className={" d-none d-lg-block p-0 p-lg-2"}>
       <PopularProfiles />
      </Col>
    </Row>
  );
}
export default PostsPage;